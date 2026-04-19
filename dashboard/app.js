// Student Performance Dashboard - JavaScript

// Mock data for dashboard (simulating API response)
const dashboardData = {
    kpi_metrics: {
        total_students: 20,
        average_math_score: 75.5,
        average_reading_score: 79.8,
        average_writing_score: 77.2,
        overall_average: 77.5,
        pass_rate: 85.0,
        top_performers_count: 5,
        top_performers_percentage: 25.0
    },
    parental_education_scores: {
        "Master's Degree": {
            count: 4,
            avg_math: 88.5,
            avg_reading: 92.0,
            avg_writing: 89.5,
            avg_overall: 90.0
        },
        "Bachelor's Degree": {
            count: 5,
            avg_math: 82.0,
            avg_reading: 85.5,
            avg_writing: 83.0,
            avg_overall: 83.5
        },
        "Associate's Degree": {
            count: 4,
            avg_math: 76.5,
            avg_reading: 79.0,
            avg_writing: 77.5,
            avg_overall: 77.7
        },
        "Some College": {
            count: 4,
            avg_math: 70.5,
            avg_reading: 74.0,
            avg_writing: 72.0,
            avg_overall: 72.2
        },
        "High School": {
            count: 3,
            avg_math: 62.0,
            avg_reading: 66.5,
            avg_writing: 64.0,
            avg_overall: 64.2
        }
    },
    gender_comparison: {
        "Male": {
            count: 10,
            avg_math: 77.0,
            avg_reading: 77.5,
            avg_writing: 75.0
        },
        "Female": {
            count: 10,
            avg_math: 74.0,
            avg_reading: 82.0,
            avg_writing: 79.5
        }
    },
    test_preparation_impact: {
        "Completed": {
            count: 10,
            avg_overall: 82.0,
            pass_rate: 95.0
        },
        "None": {
            count: 10,
            avg_overall: 73.0,
            pass_rate: 75.0
        }
    },
    subject_comparison: {
        "MathScore": {
            mean: 75.5,
            median: 76.0,
            std: 12.5,
            min: 55,
            max: 95
        },
        "ReadingScore": {
            mean: 79.8,
            median: 80.0,
            std: 11.0,
            min: 60,
            max: 98
        },
        "WritingScore": {
            mean: 77.2,
            median: 77.0,
            std: 11.5,
            min: 58,
            max: 96
        }
    }
};

// Student data for table
const studentData = [
    { id: "STU001", gender: "Male", education: "Bachelor's Degree", course: "Completed", math: 72, reading: 85, writing: 78, average: 78.3, status: "Pass" },
    { id: "STU002", gender: "Female", education: "Master's Degree", course: "Completed", math: 85, reading: 92, writing: 88, average: 88.3, status: "Pass" },
    { id: "STU003", gender: "Male", education: "Some College", course: "None", math: 65, reading: 70, writing: 68, average: 67.7, status: "Pass" },
    { id: "STU004", gender: "Female", education: "Associate's Degree", course: "Completed", math: 78, reading: 80, writing: 82, average: 80.0, status: "Pass" },
    { id: "STU005", gender: "Male", education: "High School", course: "None", math: 58, reading: 62, writing: 60, average: 60.0, status: "Pass" },
    { id: "STU006", gender: "Female", education: "Bachelor's Degree", course: "None", math: 82, reading: 88, writing: 85, average: 85.0, status: "Pass" },
    { id: "STU007", gender: "Male", education: "Master's Degree", course: "Completed", math: 90, reading: 95, writing: 92, average: 92.3, status: "Pass" },
    { id: "STU008", gender: "Female", education: "Some College", course: "Completed", math: 75, reading: 78, writing: 76, average: 76.3, status: "Pass" },
    { id: "STU009", gender: "Male", education: "High School", course: "None", math: 62, reading: 68, writing: 65, average: 65.0, status: "Pass" },
    { id: "STU010", gender: "Female", education: "Associate's Degree", course: "Completed", math: 88, reading: 90, writing: 87, average: 88.3, status: "Pass" }
];

// Business insights
const businessInsights = [
    {
        title: "Parental Education Impact",
        icon: "fas fa-graduation-cap",
        color: "purple",
        text: "Students with Master's degree parents score 25.8 points higher than those with High School educated parents. Parental education significantly impacts academic performance."
    },
    {
        title: "Gender Performance Patterns",
        icon: "fas fa-venus-mars",
        color: "blue",
        text: "Male students excel in Math (77.0) while Female students outperform in Reading (82.0) and Writing (79.5). Subject-specific strengths should inform teaching strategies."
    },
    {
        title: "Test Preparation Effectiveness",
        icon: "fas fa-book",
        color: "green",
        text: "Students who completed test preparation scored 9 points higher on average with 95% pass rate vs 75% for those without. Preparation courses are highly effective."
    },
    {
        title: "Subject Performance",
        icon: "fas fa-chart-bar",
        color: "orange",
        text: "Reading is the strongest subject (79.8 avg) while Math has highest variability. Targeted support needed for Math to reduce performance gaps."
    },
    {
        title: "Socioeconomic Factors",
        icon: "fas fa-utensils",
        color: "indigo",
        text: "Standard lunch students perform better than Free/Reduced lunch students, indicating socioeconomic factors affect academic outcomes. Support programs recommended."
    },
    {
        title: "Action Required",
        icon: "fas fa-exclamation-circle",
        color: "red",
        text: "Prioritize test preparation courses for all students, especially those from lower parental education backgrounds. Implement subject-specific tutoring for Math."
    }
];

// Initialize dashboard
document.addEventListener('DOMContentLoaded', function() {
    updateLastUpdated();
    updateKPICards();
    initializeCharts();
    populateInsights();
    populateStudentTable();
});

// Update last updated timestamp
function updateLastUpdated() {
    const now = new Date();
    document.getElementById('lastUpdated').textContent = now.toLocaleString();
}

// Update KPI cards
function updateKPICards() {
    document.getElementById('totalStudents').textContent = dashboardData.kpi_metrics.total_students;
    document.getElementById('averageScore').textContent = dashboardData.kpi_metrics.overall_average;
    document.getElementById('passRate').textContent = dashboardData.kpi_metrics.pass_rate + '%';
    document.getElementById('topPerformers').textContent = dashboardData.kpi_metrics.top_performers_count;
}

// Initialize all charts
function initializeCharts() {
    createEducationChart();
    createGenderChart();
    createPreparationChart();
    createSubjectChart();
}

// Parental Education Chart
function createEducationChart() {
    const ctx = document.getElementById('educationChart').getContext('2d');
    const educations = Object.keys(dashboardData.parental_education_scores);
    const avgScores = educations.map(edu => 
        dashboardData.parental_education_scores[edu].avg_overall
    );

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: educations,
            datasets: [{
                label: 'Average Score',
                data: avgScores,
                backgroundColor: [
                    'rgba(102, 126, 234, 0.8)',
                    'rgba(118, 75, 162, 0.8)',
                    'rgba(245, 158, 11, 0.8)',
                    'rgba(16, 185, 129, 0.8)',
                    'rgba(239, 68, 68, 0.8)'
                ],
                borderColor: [
                    'rgb(102, 126, 234)',
                    'rgb(118, 75, 162)',
                    'rgb(245, 158, 11)',
                    'rgb(16, 185, 129)',
                    'rgb(239, 68, 68)'
                ],
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100,
                    ticks: {
                        callback: function(value) {
                            return value;
                        }
                    }
                }
            }
        }
    });
}

// Gender Comparison Chart
function createGenderChart() {
    const ctx = document.getElementById('genderChart').getContext('2d');
    const genders = Object.keys(dashboardData.gender_comparison);

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: genders,
            datasets: [
                {
                    label: 'Math',
                    data: genders.map(g => dashboardData.gender_comparison[g].avg_math),
                    backgroundColor: 'rgba(59, 130, 246, 0.8)',
                    borderColor: 'rgb(59, 130, 246)',
                    borderWidth: 2
                },
                {
                    label: 'Reading',
                    data: genders.map(g => dashboardData.gender_comparison[g].avg_reading),
                    backgroundColor: 'rgba(16, 185, 129, 0.8)',
                    borderColor: 'rgb(16, 185, 129)',
                    borderWidth: 2
                },
                {
                    label: 'Writing',
                    data: genders.map(g => dashboardData.gender_comparison[g].avg_writing),
                    backgroundColor: 'rgba(245, 158, 11, 0.8)',
                    borderColor: 'rgb(245, 158, 11)',
                    borderWidth: 2
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom'
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100
                }
            }
        }
    });
}

// Test Preparation Impact Chart
function createPreparationChart() {
    const ctx = document.getElementById('preparationChart').getContext('2d');
    const courses = Object.keys(dashboardData.test_preparation_impact);

    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Completed Course', 'No Course'],
            datasets: [{
                data: courses.map(c => dashboardData.test_preparation_impact[c].avg_overall),
                backgroundColor: [
                    'rgba(16, 185, 129, 0.8)',
                    'rgba(239, 68, 68, 0.8)'
                ],
                borderColor: [
                    'rgb(16, 185, 129)',
                    'rgb(239, 68, 68)'
                ],
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom'
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return context.label + ': ' + context.raw + ' avg score';
                        }
                    }
                }
            }
        }
    });
}

// Subject Comparison Chart
function createSubjectChart() {
    const ctx = document.getElementById('subjectChart').getContext('2d');
    const subjects = Object.keys(dashboardData.subject_comparison);

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Math', 'Reading', 'Writing'],
            datasets: [{
                label: 'Mean Score',
                data: subjects.map(s => dashboardData.subject_comparison[s].mean),
                backgroundColor: [
                    'rgba(59, 130, 246, 0.8)',
                    'rgba(16, 185, 129, 0.8)',
                    'rgba(245, 158, 11, 0.8)'
                ],
                borderColor: [
                    'rgb(59, 130, 246)',
                    'rgb(16, 185, 129)',
                    'rgb(245, 158, 11)'
                ],
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100
                }
            }
        }
    });
}

// Populate insights section
function populateInsights() {
    const container = document.getElementById('insightsContainer');
    container.innerHTML = '';
    
    businessInsights.forEach(insight => {
        const card = document.createElement('div');
        card.className = 'bg-gray-50 rounded-lg p-4 border-l-4 border-' + insight.color + '-500';
        card.innerHTML = `
            <div class="flex items-start space-x-3">
                <div class="bg-${insight.color}-100 p-2 rounded-full">
                    <i class="${insight.icon} text-${insight.color}-600"></i>
                </div>
                <div>
                    <h4 class="font-semibold text-gray-800">${insight.title}</h4>
                    <p class="text-sm text-gray-600 mt-1">${insight.text}</p>
                </div>
            </div>
        `;
        container.appendChild(card);
    });
}

// Populate student table
function populateStudentTable(filteredData = studentData) {
    const tbody = document.getElementById('studentTableBody');
    tbody.innerHTML = '';
    
    filteredData.forEach(student => {
        const row = document.createElement('tr');
        row.className = 'border-b hover:bg-gray-50';
        
        const statusClass = student.status === 'Pass' ? 'text-green-600 font-semibold' : 'text-red-600';
        const statusBadge = student.status === 'Pass' 
            ? '<span class="bg-green-100 text-green-800 px-2 py-1 rounded-full text-xs">Pass</span>'
            : '<span class="bg-red-100 text-red-800 px-2 py-1 rounded-full text-xs">Fail</span>';
        
        row.innerHTML = `
            <td class="px-4 py-3 font-medium">${student.id}</td>
            <td class="px-4 py-3">${student.gender}</td>
            <td class="px-4 py-3">${student.education}</td>
            <td class="px-4 py-3">
                <span class="px-2 py-1 rounded-full text-xs ${student.course === 'Completed' ? 'bg-blue-100 text-blue-800' : 'bg-gray-100 text-gray-800'}">
                    ${student.course}
                </span>
            </td>
            <td class="px-4 py-3">${student.math}</td>
            <td class="px-4 py-3">${student.reading}</td>
            <td class="px-4 py-3">${student.writing}</td>
            <td class="px-4 py-3 font-semibold">${student.average.toFixed(1)}</td>
            <td class="px-4 py-3">${statusBadge}</td>
        `;
        tbody.appendChild(row);
    });
}

// Apply filters
function applyFilters() {
    const genderFilter = document.getElementById('genderFilter').value;
    const educationFilter = document.getElementById('educationFilter').value;
    const courseFilter = document.getElementById('courseFilter').value;
    
    let filteredData = [...studentData];
    
    if (genderFilter !== 'all') {
        filteredData = filteredData.filter(student => student.gender === genderFilter);
    }
    
    if (educationFilter !== 'all') {
        filteredData = filteredData.filter(student => student.education === educationFilter);
    }
    
    if (courseFilter !== 'all') {
        filteredData = filteredData.filter(student => student.course === courseFilter);
    }
    
    populateStudentTable(filteredData);
    
    // Show filter applied notification
    showNotification('Filters applied successfully');
}

// Reset filters
function resetFilters() {
    document.getElementById('genderFilter').value = 'all';
    document.getElementById('educationFilter').value = 'all';
    document.getElementById('courseFilter').value = 'all';
    populateStudentTable(studentData);
    showNotification('Filters reset');
}

// Show notification
function showNotification(message) {
    const notification = document.createElement('div');
    notification.className = 'fixed bottom-4 right-4 bg-green-500 text-white px-6 py-3 rounded-lg shadow-lg z-50';
    notification.innerHTML = `<i class="fas fa-check-circle mr-2"></i>${message}`;
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.remove();
    }, 3000);
}

// Simulate API call to fetch data (for demonstration)
async function fetchDashboardData() {
    try {
        // In a real application, this would be an actual API call
        // const response = await fetch('/api/performance-summary');
        // const data = await response.json();
        
        // For now, return mock data
        return dashboardData;
    } catch (error) {
        console.error('Error fetching dashboard data:', error);
        return null;
    }
}
