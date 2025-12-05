param(
    [int]$Year,
    [int]$Day
)

# Base directories
$rootDir   = Get-Location
$codeRoot  = Join-Path $rootDir 'advent_of_code'
$testRoot  = Join-Path $rootDir 'test'

# Ensure base dirs exist
if (-not (Test-Path $codeRoot)) {
    New-Item -ItemType Directory -Path $codeRoot | Out-Null
}
if (-not (Test-Path $testRoot)) {
    New-Item -ItemType Directory -Path $testRoot | Out-Null
}

#########################
# Resolve default year  #
#########################

if (-not $PSBoundParameters.ContainsKey('Year')) {
    $yearDirs = Get-ChildItem -Path $codeRoot -Directory -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -match '^year_(\d{4})$' }

    $years = foreach ($dir in $yearDirs) {
        if ($dir.Name -match '^year_(\d{4})$') {
            [int]$Matches[1]
        }
    }

    if ($years -and $years.Count -gt 0) {
        $Year = ($years | Measure-Object -Maximum).Maximum
    }
    else {
        # If no year_* dirs exist yet, fall back to current year
        $Year = (Get-Date).Year
    }
}

#########################
# Ensure year directory #
#########################

$yearDirName = "year_{0}" -f $Year
$yearDir     = Join-Path $codeRoot $yearDirName

if (-not (Test-Path $yearDir)) {
    New-Item -ItemType Directory -Path $yearDir | Out-Null
}

#########################
# Resolve default day   #
#########################

if (-not $PSBoundParameters.ContainsKey('Day')) {
    $dayDirs = Get-ChildItem -Path $yearDir -Directory -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -match '^day_(\d{2})$' }

    $days = foreach ($dir in $dayDirs) {
        if ($dir.Name -match '^day_(\d{2})$') {
            [int]$Matches[1]
        }
    }

    if ($days -and $days.Count -gt 0) {
        $Day = ($days | Measure-Object -Maximum).Maximum + 1
    }
    else {
        $Day = 1
    }
}

# Optional: enforce a reasonable AoC range
if ($Day -lt 1 -or $Day -gt 25) {
    throw "Day must be between 1 and 25. Got: $Day"
}

$dayStr     = "{0:D2}" -f $Day
$dayDirName = "day_{0}" -f $dayStr
$dayDir     = Join-Path $yearDir $dayDirName

if (-not (Test-Path $dayDir)) {
    New-Item -ItemType Directory -Path $dayDir | Out-Null
}

#############################
# Create Python code files  #
#############################

$initPath = Join-Path $dayDir '__init__.py'
$mainPath = Join-Path $dayDir 'main.py'
$inputPath = Join-Path $dayDir 'input.txt'
$dayModulePath = Join-Path $dayDir ("day_{0}.py" -f $dayStr)

# __init__.py (empty if not present)
if (-not (Test-Path $initPath)) {
    New-Item -ItemType File -Path $initPath | Out-Null
}

# main.py template
if (-not (Test-Path $mainPath)) {
    $mainContent = @"
from .day_$dayStr import solve_part1, solve_part2


def main():
    with open("input.txt") as f:
        data = f.read().strip().splitlines()
    print("Part 1:", solve_part1(data))
    print("Part 2:", solve_part2(data))


if __name__ == "__main__":
    main()
"@
    $mainContent | Set-Content -Path $mainPath -Encoding UTF8
}

# input.txt (empty if not present)
if (-not (Test-Path $inputPath)) {
    New-Item -ItemType File -Path $inputPath | Out-Null
}

# day_XX.py template
if (-not (Test-Path $dayModulePath)) {
    $dayContent = @"
def solve_part1(data):
    # TODO: implement part 1
    pass


def solve_part2(data):
    # TODO: implement part 2
    pass
"@
    $dayContent | Set-Content -Path $dayModulePath -Encoding UTF8
}

#############################
# Create test file          #
#############################

$testYearDirName = "test_{0}" -f $Year
$testYearDir     = Join-Path $testRoot $testYearDirName

if (-not (Test-Path $testYearDir)) {
    New-Item -ItemType Directory -Path $testYearDir | Out-Null
}

$testFileName = "test_{0}_day{1}.py" -f $Year, $dayStr
$testFilePath = Join-Path $testYearDir $testFileName

if (-not (Test-Path $testFilePath)) {
    $testContent = @"
import pathlib

from advent_of_code.year_$Year.day_$dayStr import solve_part1, solve_part2

# Adjust this path logic to match your test setup if needed
INPUT = (
    pathlib.Path(__file__)
    .resolve()
    .parents[2]
    / "advent_of_code"
    / "year_$Year"
    / "day_$dayStr"
    / "input.txt"
)


def test_part1():
    data = INPUT.read_text().strip().splitlines()
    assert solve_part1(data) is not None


def test_part2():
    data = INPUT.read_text().strip().splitlines()
    assert solve_part2(data) is not None
"@
    $testContent | Set-Content -Path $testFilePath -Encoding UTF8
}

Write-Host "Created scaffolding for year $Year, day $dayStr."
Write-Host "Code directory: $dayDir"
Write-Host "Test file:      $testFilePath"
