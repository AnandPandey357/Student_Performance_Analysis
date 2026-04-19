"""
Student Performance Analysis - Mock REST API Server
This Flask application provides REST API endpoints for the student performance dashboard.
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import os
import sys

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load student data
DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'raw', 'student_performance.csv')

try:
    df = pd.read_csv(DATA_PATH)
    print(f"✓ Loaded {len(df)} student records from {DATA_PATH}")
except FileNotFoundError:
    print(f"⚠ Data file not found at {DATA_PATH}")
    df = pd.DataFrame()


@app.route('/', methods=['GET'])
def home():
    """API home endpoint"""
    return jsonify({
        'message': 'Student Performance Analysis API',
        'version': '1.0.0',
        'endpoints': {
            '/students': 'GET - Get all students',
            '/students/<id>': 'GET - Get student by ID',
            '/performance-summary': 'GET - Get performance summary',
            '/subject-stats': 'GET - Get subject statistics',
            '/education-stats': 'GET - Get education level statistics'
        }
    })


@app.route('/students', methods=['GET'])
def get_students():
    """
    Get all students with optional filtering
    Query params: gender, parental_education, test_preparation
    """
    if df.empty:
        return jsonify({'error': 'No data available'}), 404
    
    # Get query parameters
    gender = request.args.get('gender')
    parental_education = request.args.get('parental_education')
    test_preparation = request.args.get('test_preparation')
    
    # Apply filters
    filtered_df = df.copy()
    
    if gender:
        filtered_df = filtered_df[filtered_df['Gender'] == gender]
    
    if parental_education:
        filtered_df = filtered_df[filtered_df['ParentalEducation'] == parental_education]
    
    if test_preparation:
        filtered_df = filtered_df[filtered_df['TestPreparationCourse'] == test_preparation]
    
    # Calculate average score for each student
    if not filtered_df.empty:
        filtered_df['AverageScore'] = (
            filtered_df['MathScore'] + filtered_df['ReadingScore'] + filtered_df['WritingScore']
        ) / 3
    
    # Convert to list of dictionaries
    students = filtered_df.to_dict(orient='records')
    
    return jsonify({
        'total': len(students),
        'data': students
    })


@app.route('/students/<student_id>', methods=['GET'])
def get_student_by_id(student_id):
    """Get a specific student by ID"""
    if df.empty:
        return jsonify({'error': 'No data available'}), 404
    
    student = df[df['StudentID'] == student_id]
    
    if student.empty:
        return jsonify({'error': 'Student not found'}), 404
    
    # Calculate average score
    student_dict = student.to_dict(orient='records')[0]
    student_dict['AverageScore'] = (
        student_dict['MathScore'] + student_dict['ReadingScore'] + student_dict['WritingScore']
    ) / 3
    
    return jsonify(student_dict)


@app.route('/performance-summary', methods=['GET'])
def get_performance_summary():
    """
    Get comprehensive performance summary
    Includes: overall statistics, pass rates, top performers
    """
    if df.empty:
        return jsonify({'error': 'No data available'}), 404
    
    total_students = len(df)
    
    # Calculate averages
    avg_math = df['MathScore'].mean()
    avg_reading = df['ReadingScore'].mean()
    avg_writing = df['WritingScore'].mean()
    avg_overall = (avg_math + avg_reading + avg_writing) / 3
    
    # Calculate pass rate (assuming 60 as passing)
    df['AverageScore'] = (df['MathScore'] + df['ReadingScore'] + df['WritingScore']) / 3
    pass_count = len(df[df['AverageScore'] >= 60])
    pass_rate = (pass_count / total_students) * 100 if total_students > 0 else 0
    
    # Top performers (score >= 90)
    top_performers = len(df[df['AverageScore'] >= 90])
    
    # Performance by gender
    gender_stats = {}
    for gender in df['Gender'].unique():
        gender_data = df[df['Gender'] == gender]
        gender_stats[gender] = {
            'count': len(gender_data),
            'average_score': round(gender_data['AverageScore'].mean(), 2),
            'pass_rate': round(len(gender_data[gender_data['AverageScore'] >= 60]) / len(gender_data) * 100, 2)
        }
    
    # Performance by test preparation
    course_stats = {}
    for course in df['TestPreparationCourse'].unique():
        course_data = df[df['TestPreparationCourse'] == course]
        course_stats[course] = {
            'count': len(course_data),
            'average_score': round(course_data['AverageScore'].mean(), 2),
            'pass_rate': round(len(course_data[course_data['AverageScore'] >= 60]) / len(course_data) * 100, 2)
        }
    
    return jsonify({
        'overall': {
            'total_students': int(total_students),
            'average_math_score': round(avg_math, 2),
            'average_reading_score': round(avg_reading, 2),
            'average_writing_score': round(avg_writing, 2),
            'overall_average': round(avg_overall, 2),
            'pass_rate': round(pass_rate, 2),
            'top_performers_count': int(top_performers)
        },
        'by_gender': gender_stats,
        'by_test_preparation': course_stats
    })


@app.route('/subject-stats', methods=['GET'])
def get_subject_stats():
    """Get statistics by subject"""
    if df.empty:
        return jsonify({'error': 'No data available'}), 404
    
    subject_stats = {
        'MathScore': {
            'mean': round(df['MathScore'].mean(), 2),
            'median': round(df['MathScore'].median(), 2),
            'std': round(df['MathScore'].std(), 2),
            'min': int(df['MathScore'].min()),
            'max': int(df['MathScore'].max())
        },
        'ReadingScore': {
            'mean': round(df['ReadingScore'].mean(), 2),
            'median': round(df['ReadingScore'].median(), 2),
            'std': round(df['ReadingScore'].std(), 2),
            'min': int(df['ReadingScore'].min()),
            'max': int(df['ReadingScore'].max())
        },
        'WritingScore': {
            'mean': round(df['WritingScore'].mean(), 2),
            'median': round(df['WritingScore'].median(), 2),
            'std': round(df['WritingScore'].std(), 2),
            'min': int(df['WritingScore'].min()),
            'max': int(df['WritingScore'].max())
        }
    }
    
    return jsonify(subject_stats)


@app.route('/education-stats', methods=['GET'])
def get_education_stats():
    """Get statistics by parental education level"""
    if df.empty:
        return jsonify({'error': 'No data available'}), 404
    
    df['AverageScore'] = (df['MathScore'] + df['ReadingScore'] + df['WritingScore']) / 3
    
    education_stats = {}
    for edu in df['ParentalEducation'].unique():
        edu_data = df[df['ParentalEducation'] == edu]
        education_stats[edu] = {
            'count': int(len(edu_data)),
            'average_math': round(edu_data['MathScore'].mean(), 2),
            'average_reading': round(edu_data['ReadingScore'].mean(), 2),
            'average_writing': round(edu_data['WritingScore'].mean(), 2),
            'average_overall': round(edu_data['AverageScore'].mean(), 2),
            'pass_rate': round(len(edu_data[edu_data['AverageScore'] >= 60]) / len(edu_data) * 100, 2)
        }
    
    return jsonify(education_stats)


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    print("=" * 60)
    print("STUDENT PERFORMANCE ANALYSIS API SERVER")
    print("=" * 60)
    print("\nAvailable Endpoints:")
    print("  GET  /                    - API information")
    print("  GET  /students           - Get all students")
    print("  GET  /students/<id>      - Get student by ID")
    print("  GET  /performance-summary - Get performance summary")
    print("  GET  /subject-stats       - Get subject statistics")
    print("  GET  /education-stats     - Get education statistics")
    print("\nServer starting on http://localhost:5000")
    print("=" * 60)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
