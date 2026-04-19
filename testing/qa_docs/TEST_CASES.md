# Test Cases - Student Performance Analysis Dashboard

## Document Information
- **Project Name**: Student Performance Analysis Dashboard
- **Document Version**: 1.0
- **Test Suite**: Functional, Data Validation & UI Testing

## 1. Data Validation Test Cases

### TC-DV-001: Score Range Validation
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-DV-001 |
| **Title** | Verify scores are within valid range (0-100) |
| **Description** | Ensure all Math, Reading, and Writing scores are between 0 and 100 |
| **Preconditions** | Raw dataset loaded |
| **Test Steps** | 1. Run data_validation.py<br>2. Check score range validation results<br>3. Verify no scores outside 0-100 range |
| **Expected Result** | All scores within valid range (0-100) |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | Critical |

### TC-DV-002: Duplicate Record Detection
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-DV-002 |
| **Title** | Verify duplicate record detection |
| **Description** | Ensure the validation script identifies duplicate StudentIDs |
| **Preconditions** | Raw dataset with potential duplicates |
| **Test Steps** | 1. Add duplicate StudentID to dataset<br>2. Run data_validation.py<br>3. Verify duplicates are detected |
| **Expected Result** | Duplicate StudentIDs identified and reported |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | Critical |

### TC-DV-003: Null Value Detection
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-DV-003 |
| **Title** | Verify null value detection and reporting |
| **Description** | Ensure the validation script identifies missing/null values |
| **Preconditions** | Raw dataset with null values |
| **Test Steps** | 1. Add null values to dataset<br>2. Run data_validation.py<br>3. Verify null values are detected |
| **Expected Result** | Null values detected and reported with counts |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | High |

### TC-DV-004: Data Consistency Validation
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-DV-004 |
| **Title** | Verify categorical data consistency |
| **Description** | Ensure categorical values match expected values |
| **Preconditions** | Raw dataset loaded |
| **Test Steps** | 1. Run data_validation.py<br>2. Check consistency validation results<br>3. Verify no unexpected categorical values |
| **Expected Result** | All categorical values are consistent and valid |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | High |

### TC-DV-005: Edge Case - Zero Scores
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-DV-005 |
| **Title** | Verify detection of zero scores (potential missing data) |
| **Description** | Ensure edge case simulation identifies zero scores |
| **Preconditions** | Dataset with zero scores |
| **Test Steps** | 1. Run data_validation.py<br>2. Check edge case results<br>3. Verify zero scores are flagged |
| **Expected Result** | Zero scores identified as edge cases |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | Medium |

### TC-DV-006: Edge Case - Perfect Scores
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-DV-006 |
| **Title** | Verify detection of perfect scores (100) |
| **Description** | Ensure edge case simulation identifies perfect scores |
| **Preconditions** | Dataset with scores of 100 |
| **Test Steps** | 1. Run data_validation.py<br>2. Check edge case results<br>3. Verify perfect scores are flagged |
| **Expected Result** | Perfect scores identified as edge cases |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | Low |

## 2. API Test Cases

### TC-API-001: API Home Endpoint
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-API-001 |
| **Title** | Verify API home endpoint returns correct information |
| **Description** | Test GET / endpoint returns API information |
| **Preconditions** | Flask server running on localhost:5000 |
| **Test Steps** | 1. Send GET request to http://localhost:5000/<br>2. Verify status code is 200<br>3. Verify response has message and endpoints fields |
| **Expected Result** | Status 200, response contains message and endpoints |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | High |

### TC-API-002: Get All Students
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-API-002 |
| **Title** | Verify GET /students returns all student data |
| **Description** | Test GET /students endpoint returns complete student dataset |
| **Preconditions** | Flask server running |
| **Test Steps** | 1. Send GET request to /students<br>2. Verify status code is 200<br>3. Verify response has data array<br>4. Verify data has required fields |
| **Expected Result** | Status 200, data array with all student records |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | High |

### TC-API-003: Get Student by ID
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-API-003 |
| **Title** | Verify GET /students/<id> returns specific student |
| **Description** | Test GET /students/<id> endpoint returns correct student record |
| **Preconditions** | Flask server running, valid student ID exists |
| **Test Steps** | 1. Send GET request to /students/STU001<br>2. Verify status code is 200<br>3. Verify StudentID matches request |
| **Expected Result** | Status 200, student record with correct ID |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | High |

### TC-API-004: Invalid Student ID
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-API-004 |
| **Title** | Verify GET /students/<invalid-id> returns 404 |
| **Description** | Test edge case: invalid student ID returns 404 error |
| **Preconditions** | Flask server running |
| **Test Steps** | 1. Send GET request to /students/INVALID999<br>2. Verify status code is 404<br>3. Verify error message in response |
| **Expected Result** | Status 404, error message returned |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | Medium |

### TC-API-005: Filter by Gender
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-API-005 |
| **Title** | Verify gender filter functionality |
| **Description** | Test GET /students?gender=Male filters correctly |
| **Preconditions** | Flask server running |
| **Test Steps** | 1. Send GET request with gender parameter<br>2. Verify status code is 200<br>3. Verify all results are from specified gender |
| **Expected Result** | Status 200, all students from specified gender |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | High |

### TC-API-006: Get Performance Summary
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-API-006 |
| **Title** | Verify GET /performance-summary returns comprehensive statistics |
| **Description** | Test GET /performance-summary endpoint returns all required statistics |
| **Preconditions** | Flask server running |
| **Test Steps** | 1. Send GET request to /performance-summary<br>2. Verify status code is 200<br>3. Verify response has overall, by_gender, by_test_preparation |
| **Expected Result** | Status 200, comprehensive performance statistics |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | High |

### TC-API-007: Get Subject Statistics
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-API-007 |
| **Title** | Verify GET /subject-stats returns subject statistics |
| **Description** | Test GET /subject-stats endpoint returns statistics for all subjects |
| **Preconditions** | Flask server running |
| **Test Steps** | 1. Send GET request to /subject-stats<br>2. Verify status code is 200<br>3. Verify response has MathScore, ReadingScore, WritingScore |
| **Expected Result** | Status 200, statistics for all three subjects |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | High |

## 3. Functional Test Cases - Dashboard

### TC-UI-001: Dashboard Page Loading
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-UI-001 |
| **Title** | Verify dashboard page loads correctly |
| **Description** | Test that the dashboard HTML page loads without errors |
| **Preconditions** | Dashboard file exists at dashboard/index.html |
| **Test Steps** | 1. Open dashboard in browser<br>2. Verify page title<br>3. Verify header displayed<br>4. Verify heading displayed |
| **Expected Result** | Page loads with correct title, header, and heading |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | High |

### TC-UI-002: KPI Cards Display
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-UI-002 |
| **Title** | Verify KPI cards display with correct data |
| **Description** | Test that all 4 KPI cards are displayed with valid data |
| **Preconditions** | Dashboard loaded |
| **Test Steps** | 1. Verify Total Students card displayed<br>2. Verify Average Score card displayed<br>3. Verify Pass Rate card displayed<br>4. Verify Top Performers card displayed<br>5. Verify values are non-zero |
| **Expected Result** | All 4 KPI cards displayed with valid data |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | High |

### TC-UI-003: Charts Rendering
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-UI-003 |
| **Title** | Verify all charts render correctly |
| **Description** | Test that all 4 charts are rendered on the dashboard |
| **Preconditions** | Dashboard loaded, JavaScript executed |
| **Test Steps** | 1. Verify Parental Education chart rendered<br>2. Verify Gender Comparison chart rendered<br>3. Verify Test Preparation chart rendered<br>4. Verify Subject Comparison chart rendered |
| **Expected Result** | All 4 charts displayed correctly |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | High |

### TC-UI-004: Filter Functionality
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-UI-004 |
| **Title** | Verify filter functionality works correctly |
| **Description** | Test that department filter filters student table correctly |
| **Preconditions** | Dashboard loaded |
| **Test Steps** | 1. Note initial student count<br>2. Select "Male" from gender filter<br>3. Click "Apply Filters"<br>4. Verify table shows only Male students<br>5. Click "Reset"<br>6. Verify original count restored |
| **Expected Result** | Filter works correctly, reset restores data |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | High |

### TC-UI-005: Student Table Data
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-UI-005 |
| **Title** | Verify student table contains valid data |
| **Description** | Test that student table displays correct data with proper formatting |
| **Preconditions** | Dashboard loaded |
| **Test Steps** | 1. Verify table has 9 columns<br>2. Verify Student ID format (STU###)<br>3. Verify scores are numeric<br>4. Verify Pass/Fail badge displayed |
| **Expected Result** | Table has correct columns and valid data |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | Medium |

### TC-UI-006: Insights Section
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-UI-006 |
| **Title** | Verify insights section is populated |
| **Description** | Test that insights section displays business insights |
| **Preconditions** | Dashboard loaded |
| **Test Steps** | 1. Verify insights container displayed<br>2. Verify insight cards present<br>3. Verify each card has title and text |
| **Expected Result** | Insights section populated with business insights |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | Medium |

## 4. Negative Test Cases

### TC-NEG-001: Invalid Gender Filter
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-NEG-001 |
| **Title** | Verify invalid gender filter returns empty results |
| **Description** | Test negative case: invalid gender filter value |
| **Preconditions** | API server running |
| **Test Steps** | 1. Send GET request with gender=InvalidGender<br>2. Verify status code is 200<br>3. Verify returns empty data array |
| **Expected Result** | Status 200, empty data array |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | Medium |

### TC-NEG-002: Missing Required Fields
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-NEG-002 |
| **Title** | Validate response schema for missing fields |
| **Description** | Test that API response contains all required fields |
| **Preconditions** | API server running |
| **Test Steps** | 1. Send GET request to /students<br>2. Verify response contains all required fields<br>3. Check for StudentID, Gender, Scores, AverageScore |
| **Expected Result** | All required fields present in response |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | High |

### TC-NEG-003: Out of Range Scores
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-NEG-003 |
| **Title** | Verify detection of out-of-range scores |
| **Description** | Test validation catches scores outside 0-100 range |
| **Preconditions** | Dataset with invalid scores |
| **Test Steps** | 1. Add score of 150 to dataset<br>2. Run data_validation.py<br>3. Verify out-of-range score detected |
| **Expected Result** | Out-of-range score flagged as violation |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | Critical |

## Test Summary

| Category | Total | Passed | Failed | Pending |
|----------|-------|--------|--------|---------|
| Data Validation | 6 | 0 | 0 | 6 |
| API Tests | 7 | 0 | 0 | 7 |
| Dashboard UI | 6 | 0 | 0 | 6 |
| Negative Tests | 3 | 0 | 0 | 3 |
| **Total** | **22** | **0** | **0** | **22** |

## Test Execution Notes

- All test cases to be executed in sequence
- Postman collection for API tests (TC-API-001 to TC-API-007)
- Python scripts for data validation tests (TC-DV-001 to TC-DV-006)
- Manual testing for dashboard UI (TC-UI-001 to TC-UI-006)
- Negative testing across all modules (TC-NEG-001 to TC-NEG-003)
