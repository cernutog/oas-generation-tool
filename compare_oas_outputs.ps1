# Regression Test: Compare OAS Generated Files
# Compares the two most recent files for each base name
# Usage: .\compare_oas_outputs.ps1

$OutputFolder = "OAS Generated"
$ReportFile = "regression_test_report.txt"

Write-Host "=== OAS Regression Test ===" -ForegroundColor Cyan
Write-Host "Analyzing files in: $OutputFolder`n" -ForegroundColor Gray

# Get all YAML files
$yamlFiles = Get-ChildItem -Path $OutputFolder -Filter "*.yaml" | 
    Where-Object { $_.Name -like "EBACL_FPAD_*" }

if ($yamlFiles.Count -eq 0) {
    Write-Host "No YAML files found matching pattern EBACL_FPAD_*" -ForegroundColor Yellow
    exit 1
}

# Group files by base name (everything after the date)
$fileGroups = $yamlFiles | Group-Object {
    # Extract base name: remove "EBACL_FPAD_YYYYMMDD_" prefix
    $_.Name -replace '^EBACL_FPAD_\d{8}_', ''
}

$testResults = @()
$totalGroups = 0
$identicalGroups = 0
$differentGroups = 0

foreach ($group in $fileGroups) {
    $totalGroups++
    $baseName = $group.Name
    $files = $group.Group | Sort-Object LastWriteTime -Descending
    
    if ($files.Count -lt 2) {
        Write-Host "⚠ Skipping $baseName (only 1 file found)" -ForegroundColor Yellow
        continue
    }
    
    # Compare the two most recent files
    $newFile = $files[0].FullName
    $oldFile = $files[1].FullName
    
    Write-Host "Testing: $baseName" -ForegroundColor White
    Write-Host "  Old: $($files[1].Name)" -ForegroundColor Gray
    Write-Host "  New: $($files[0].Name)" -ForegroundColor Gray
    
    # Binary comparison
    $diff = fc.exe /b $oldFile $newFile 2>&1
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  ✓ IDENTICAL" -ForegroundColor Green
        $identicalGroups++
        $testResults += [PSCustomObject]@{
            BaseName = $baseName
            Status = "PASS"
            OldFile = $files[1].Name
            NewFile = $files[0].Name
            Differences = 0
        }
    } else {
        Write-Host "  ✗ DIFFERENT" -ForegroundColor Red
        $differentGroups++
        
        # Count differences
        $diffCount = ($diff | Select-String "FC:" | Measure-Object).Count
        
        $testResults += [PSCustomObject]@{
            BaseName = $baseName
            Status = "FAIL"
            OldFile = $files[1].Name
            NewFile = $files[0].Name
            Differences = $diffCount
        }
    }
    Write-Host ""
}

# Generate report
$report = @"
=== OAS Regression Test Report ===
Generated: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")

SUMMARY:
--------
Total file groups tested: $totalGroups
✓ Identical (PASS): $identicalGroups
✗ Different (FAIL): $differentGroups

DETAILED RESULTS:
-----------------
"@

foreach ($result in $testResults) {
    $statusSymbol = if ($result.Status -eq "PASS") { "✓" } else { "✗" }
    $report += "`n$statusSymbol $($result.BaseName)"
    $report += "`n  Old: $($result.OldFile)"
    $report += "`n  New: $($result.NewFile)"
    if ($result.Status -eq "FAIL") {
        $report += "`n  Differences: $($result.Differences) byte ranges"
    }
    $report += "`n"
}

$report | Out-File -FilePath $ReportFile -Encoding UTF8

Write-Host "=== FINAL RESULTS ===" -ForegroundColor Cyan
Write-Host "Total Groups: $totalGroups" -ForegroundColor White
Write-Host "✓ PASS: $identicalGroups" -ForegroundColor Green
Write-Host "✗ FAIL: $differentGroups" -ForegroundColor Red
Write-Host "`nFull report saved to: $ReportFile`n" -ForegroundColor Gray

if ($differentGroups -eq 0) {
    Write-Host "🎉 ALL TESTS PASSED! Refactoring is regression-free." -ForegroundColor Green
    exit 0
} else {
    Write-Host "⚠ REGRESSION DETECTED! Please review differences." -ForegroundColor Yellow
    exit 1
}
