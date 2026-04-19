# Bug Report Samples - Student Performance Analysis Dashboard

## Document Information
- **Project Name**: Student Performance Analysis Dashboard
- **Document Version**: 1.0
- **Purpose**: Sample bug reports for reference

---

## Bug Report #1 - Critical

| Field | Details |
|-------|---------|
| **Bug ID** | BUG-001 |
| **Title** | Data validation script fails to detect scores > 100 |
| **Severity** | Critical |
| **Priority** | P1 |
| **Status** | Open |
| **Reported By** | QA Engineer |
| **Reported Date** | 2024-01-20 |
| **Assigned To** | Developer |
| **Environment** | Development |

### Description
The data validation script does not properly detect scores greater than 100 when they are present in the dataset. This allows invalid data to pass through validation, compromising data integrity.

### Steps to Reproduce
1. Add a record with MathScore = 150 to the dataset
2. Run data_validation.py
3. Check the validation report
4. Observe that the out-of-range score is not flagged

### Expected Behavior
The validation script should detect scores > 100 and flag them as range violations.

### Actual Behavior
Scores > 100 are not detected by the validation script.

### Error Message
No error message; the script completes successfully without flagging the violation.

### Root Cause
The score range validation logic has a bug in the comparison operator.

### Suggested Fix
```python
# Current (incorrect)
invalid = self.df[(self.df[col] <= 0) | (self.df[col] >= 100)]

# Fixed
invalid = self.df[(self.df[col] < 0) | (self.df[col] > 100)]
```

### Attachments
- Screenshot of validation report showing no violations
- Sample dataset with score = 150

---

## Bug Report #2 - High

| Field | Details |
|-------|---------|
| **Bug ID** | BUG-002 |
| **Title** | Dashboard displays incorrect average calculation |
| **Severity** | High |
| **Priority** | P1 |
| **Status** | Open |
| **Reported By** | QA Engineer |
| **Reported Date** | 2024-01-21 |
| **Assigned To** | Frontend Developer |
| **Environment** | Production |

### Description
The dashboard KPI card for "Average Score" displays an incorrect value. The calculated average does not match the manual calculation from the raw data.

### Steps to Reproduce
1. Open dashboard in browser
2. Note the Average Score displayed in KPI card
3. Manually calculate average from student data
4. Compare the values

### Expected Behavior
Average Score should match manual calculation: (sum of all scores) / (number of students * 3)

### Actual Behavior
Dashboard shows average of 77.5, but manual calculation yields 76.8

### Root Cause
JavaScript calculation in app.js uses incorrect formula or includes only a subset of students.

### Suggested Fix
```javascript
// Ensure all students are included in calculation
const totalAverage = (mathSum + readingSum + writingSum) / (studentCount * 3);
```

### Attachments
- Screenshot of dashboard KPI card
- Manual calculation worksheet

---

## Bug Report #3 - Medium

| Field | Details |
|-------|---------|
| **Bug ID** | BUG-003 |
| **Title** | Filter reset does not restore all students |
| **Severity** | Medium |
| **Priority** | P2 |
| **Status** | Open |
| **Reported By** | QA Engineer |
| **Reported Date** | 2024-01-22 |
| **Assigned To** | Frontend Developer |
| **Environment** | Development |

### Description
After applying a gender filter and clicking the Reset button, the student table does not restore to show all students. It continues to show only the filtered results.

### Steps to Reproduce
1. Open dashboard in browser
2. Select "Male" from gender filter
3. Click "Apply Filters"
4. Verify table shows only Male students
5. Click "Reset" button
6. Observe student table

### Expected Behavior
After clicking Reset, the student table should display all students from all genders.

### Actual Behavior
Student table continues to show only Male students after reset.

### Root Cause
JavaScript resetFilters() function does not properly reset the filter state.

### Suggested Fix
```javascript
function resetFilters() {
    document.getElementById('genderFilter').value = 'all';
    document.getElementById('educationFilter').value = 'all';
    document.getElementById('courseFilter').value = 'all';
    populateStudentTable(studentData);  // Use original data
    showNotification('Filters reset');
}
```

### Attachments
- Video recording of the issue
- Browser console output

---

## Bug Report #4 - Medium

| Field | Details |
|-------|---------|
| **Bug ID** | BUG-004 |
| **Title** | API returns incorrect pass rate calculation |
| **Severity** | Medium |
| **Priority** | P2 |
| **Status** | Open |
| **Reported By** | QA Engineer |
| **Reported Date** | 2024-01-23 |
| **Assigned To** | Backend Developer |
| **Environment** | Development |

### Description
The /performance-summary endpoint returns an incorrect pass rate. The API calculates pass rate as 85%, but manual calculation shows it should be 90%.

### Steps to Reproduce
1. Start API server
2. Send GET request to /performance-summary
3. Note the pass_rate value in response
4. Manually calculate pass rate from student data

### Expected Behavior
Pass rate should be: (students with average >= 60) / total students * 100

### Actual Behavior
API returns 85%, manual calculation yields 90%

### Root Cause
Pass threshold in API calculation is set to 65 instead of 60.

### Suggested Fix
```python
# Current (incorrect)
pass_count = len(df[df['AverageScore'] >= 65])

# Fixed
pass_count = len(df[df['AverageScore'] >= 60])
```

### Attachments
- API response JSON showing incorrect pass rate
- Manual calculation verification

---

## Bug Report #5 - Low

| Field | Details |
|-------|---------|
| **Bug ID** | BUG-005 |
| **Title** | Typo in dashboard footer text |
| **Severity** | Low |
| **Priority** | P3 |
| **Status** | Open |
| **Reported By** | QA Engineer |
| **Reported Date** | 2024-01-24 |
| **Assigned To** | Frontend Developer |
| **Environment** | Production |

### Description
The dashboard footer contains a typo: "Performace" instead of "Performance" in the copyright text.

### Steps to Reproduce
1. Open dashboard in browser
2. Scroll to footer section
3. Read the footer text

### Expected Behavior
Footer should read: "Student Performance Analysis Dashboard"

### Actual Behavior
Footer reads: "Student Performace Analysis Dashboard"

### Root Cause
Typo in HTML footer element.

### Suggested Fix
Correct the spelling in dashboard/index.html:
```html
<p class="text-sm">
    <i class="fas fa-graduation-cap mr-2"></i>
    Student Performance Analysis Dashboard | Built with HTML, CSS, JavaScript & Chart.js
</p>
```

### Attachments
- Screenshot of footer with typo

---

## Bug Report #6 - Low

| Field | Details |
|-------|---------|
| **Bug ID** | BUG-006 |
| **Title** | Chart colors not colorblind-friendly |
| **Severity** | Low |
| **Priority** | P3 |
| **Status** | Open |
| **Reported By** | QA Engineer |
| **Reported Date** | 2024-01-25 |
| **Assigned To** | Frontend Developer |
| **Environment** | Development |

### Description
The chart colors in the dashboard use red/green combinations that are not accessible for colorblind users.

### Steps to Reproduce
1. Open dashboard in browser
2. Use colorblind accessibility checker
3. Verify chart color contrast

### Expected Behavior
Charts should use colorblind-friendly color palette.

### Actual Behavior
Charts use red/green color combinations that are difficult for colorblind users to distinguish.

### Root Cause
Chart.js color configuration does not consider accessibility.

### Suggested Fix
Use colorblind-friendly palette:
```javascript
backgroundColor: [
    'rgba(59, 130, 246, 0.8)',   // Blue
    'rgba(245, 158, 11, 0.8)',   // Amber
    'rgba(16, 185, 129, 0.8)',   // Green
    'rgba(139, 92, 246, 0.8)'    // Purple
]
```

### Attachments
- Accessibility audit report
- Colorblind simulation screenshots

---

## Bug Summary Report

| Severity | Count | Percentage |
|----------|-------|------------|
| Critical | 1 | 16.7% |
| High | 1 | 16.7% |
| Medium | 2 | 33.3% |
| Low | 2 | 33.3% |
| **Total** | **6** | **100%** |

### Bug Status Distribution

| Status | Count |
|--------|-------|
| Open | 6 |
| In Progress | 0 |
| Resolved | 0 |
| Closed | 0 |

### Priority Distribution

| Priority | Count |
|----------|-------|
| P1 | 2 |
| P2 | 2 |
| P3 | 2 |

### Recommendations

1. **Immediate Action**: Fix BUG-001 (Critical) and BUG-002 (High) before release
2. **Short-term**: Address BUG-003 and BUG-004 in next sprint
3. **Long-term**: Fix cosmetic issues (BUG-005, BUG-006) when time permits
4. **Process Improvement**: Add automated validation tests to catch similar bugs early
5. **Accessibility**: Implement colorblind-friendly design standards
