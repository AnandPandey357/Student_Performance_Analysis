"""
Student Performance Analysis - Data Validation & Quality Checks Script
This script performs comprehensive data validation, quality checks, and edge case testing.
"""

import pandas as pd
import numpy as np
import json
import os
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class DataValidator:
    """Handle all data validation and quality checks"""
    
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = None
        self.validation_results = {}
        self.quality_metrics = {}
        self.edge_cases = []
        
    def load_data(self):
        """Load the dataset"""
        logger.info("Loading dataset for validation...")
        self.df = pd.read_csv(self.data_path)
        logger.info(f"Dataset loaded: {self.df.shape[0]} rows, {self.df.shape[1]} columns")
        return self.df
    
    def validate_score_ranges(self):
        """
        Validate that all scores are within valid range (0-100)
        Range validation is critical for data integrity
        """
        logger.info("\n=== SCORE RANGE VALIDATION ===")
        
        score_columns = ['MathScore', 'ReadingScore', 'WritingScore']
        range_violations = {}
        
        for col in score_columns:
            # Check for negative scores
            negative = self.df[self.df[col] < 0]
            # Check for scores > 100
            above_100 = self.df[self.df[col] > 100]
            
            violations = {
                'negative_count': len(negative),
                'negative_records': negative[['StudentID', col]].to_dict('records') if len(negative) > 0 else [],
                'above_100_count': len(above_100),
                'above_100_records': above_100[['StudentID', col]].to_dict('records') if len(above_100) > 0 else []
            }
            
            total_violations = violations['negative_count'] + violations['above_100_count']
            
            if total_violations > 0:
                logger.warning(f"⚠ {col}: {total_violations} range violations detected")
                range_violations[col] = violations
            else:
                logger.info(f"✓ {col}: All scores within valid range (0-100)")
        
        self.validation_results['score_range_validation'] = {
            'passed': len(range_violations) == 0,
            'violations': range_violations
        }
        
        return range_violations
    
    def detect_duplicate_records(self):
        """
        Detect duplicate records based on StudentID
        Duplicate detection prevents data redundancy
        """
        logger.info("\n=== DUPLICATE RECORD DETECTION ===")
        
        # Check for exact duplicates
        exact_duplicates = self.df.duplicated()
        exact_duplicate_count = exact_duplicates.sum()
        
        # Check for duplicate StudentIDs
        student_id_duplicates = self.df.duplicated(subset=['StudentID'], keep=False)
        duplicate_student_ids = self.df[student_id_duplicates]['StudentID'].unique()
        
        logger.info(f"Exact duplicate records: {exact_duplicate_count}")
        logger.info(f"Duplicate StudentIDs: {len(duplicate_student_ids)}")
        
        if len(duplicate_student_ids) > 0:
            logger.warning(f"⚠ Duplicate StudentIDs found: {list(duplicate_student_ids)}")
        
        self.validation_results['duplicate_detection'] = {
            'exact_duplicate_count': int(exact_duplicate_count),
            'duplicate_student_ids': list(duplicate_student_ids),
            'passed': exact_duplicate_count == 0 and len(duplicate_student_ids) == 0
        }
        
        return exact_duplicate_count, duplicate_student_ids
    
    def validate_null_values(self):
        """
        Validate and report null/missing values
        Null value handling ensures data completeness
        """
        logger.info("\n=== NULL VALUE VALIDATION ===")
        
        null_counts = self.df.isnull().sum()
        null_percentage = (null_counts / len(self.df) * 100).round(2)
        
        null_report = {}
        has_nulls = False
        
        for col in self.df.columns:
            if null_counts[col] > 0:
                has_nulls = True
                null_report[col] = {
                    'count': int(null_counts[col]),
                    'percentage': float(null_percentage[col])
                }
                logger.warning(f"⚠ {col}: {null_counts[col]} null values ({null_percentage[col]}%)")
        
        if not has_nulls:
            logger.info("✓ No null values detected")
        
        self.validation_results['null_validation'] = {
            'has_nulls': has_nulls,
            'null_report': null_report,
            'passed': not has_nulls
        }
        
        return null_report
    
    def validate_data_consistency(self):
        """
        Validate data consistency across related fields
        Consistency checks ensure logical data relationships
        """
        logger.info("\n=== DATA CONSISTENCY VALIDATION ===")
        
        inconsistencies = {}
        
        # Check 1: Parental Education values
        valid_education = ['High School', 'Some College', "Associate's Degree", 
                          "Bachelor's Degree", "Master's Degree"]
        invalid_education = self.df[~self.df['ParentalEducation'].isin(valid_education)]
        if len(invalid_education) > 0:
            logger.warning(f"⚠ Invalid ParentalEducation values: {len(invalid_education)} records")
            inconsistencies['invalid_education'] = len(invalid_education)
        
        # Check 2: Gender values
        valid_gender = ['Male', 'Female']
        invalid_gender = self.df[~self.df['Gender'].isin(valid_gender)]
        if len(invalid_gender) > 0:
            logger.warning(f"⚠ Invalid Gender values: {len(invalid_gender)} records")
            inconsistencies['invalid_gender'] = len(invalid_gender)
        
        # Check 3: LunchType values
        valid_lunch = ['Standard', 'Free/Reduced']
        invalid_lunch = self.df[~self.df['LunchType'].isin(valid_lunch)]
        if len(invalid_lunch) > 0:
            logger.warning(f"⚠ Invalid LunchType values: {len(invalid_lunch)} records")
            inconsistencies['invalid_lunch'] = len(invalid_lunch)
        
        # Check 4: TestPreparationCourse values
        valid_course = ['Completed', 'None']
        invalid_course = self.df[~self.df['TestPreparationCourse'].isin(valid_course)]
        if len(invalid_course) > 0:
            logger.warning(f"⚠ Invalid TestPreparationCourse values: {len(invalid_course)} records")
            inconsistencies['invalid_course'] = len(invalid_course)
        
        if inconsistencies:
            logger.warning(f"⚠ Total inconsistencies: {sum(inconsistencies.values())}")
        else:
            logger.info("✓ All categorical values are consistent")
        
        self.validation_results['consistency_validation'] = {
            'inconsistencies': inconsistencies,
            'passed': len(inconsistencies) == 0
        }
        
        return inconsistencies
    
    def simulate_edge_cases(self):
        """
        Simulate and test edge cases for robustness
        Edge case testing ensures system reliability
        """
        logger.info("\n=== EDGE CASE SIMULATION ===")
        
        edge_cases = []
        
        # Edge Case 1: Missing scores (simulate by checking for zeros)
        zero_scores = self.df[(self.df['MathScore'] == 0) | 
                              (self.df['ReadingScore'] == 0) | 
                              (self.df['WritingScore'] == 0)]
        if len(zero_scores) > 0:
            edge_cases.append({
                'type': 'missing_scores',
                'description': 'Students with zero scores (potential missing data)',
                'count': len(zero_scores),
                'records': zero_scores['StudentID'].tolist()
            })
            logger.warning(f"⚠ Edge case: {len(zero_scores)} students with zero scores")
        
        # Edge Case 2: Perfect scores (100)
        perfect_scores = self.df[(self.df['MathScore'] == 100) | 
                                 (self.df['ReadingScore'] == 100) | 
                                 (self.df['WritingScore'] == 100)]
        if len(perfect_scores) > 0:
            edge_cases.append({
                'type': 'perfect_scores',
                'description': 'Students with perfect scores',
                'count': len(perfect_scores),
                'records': perfect_scores['StudentID'].tolist()
            })
            logger.info(f"ℹ Edge case: {len(perfect_scores)} students with perfect scores")
        
        # Edge Case 3: Extremely low scores (< 30)
        low_scores = self.df[(self.df['MathScore'] < 30) | 
                            (self.df['ReadingScore'] < 30) | 
                            (self.df['WritingScore'] < 30)]
        if len(low_scores) > 0:
            edge_cases.append({
                'type': 'extremely_low_scores',
                'description': 'Students with extremely low scores (< 30)',
                'count': len(low_scores),
                'records': low_scores['StudentID'].tolist()
            })
            logger.warning(f"⚠ Edge case: {len(low_scores)} students with extremely low scores")
        
        # Edge Case 4: Score discrepancies (large variance between subjects)
        self.df['ScoreVariance'] = self.df[['MathScore', 'ReadingScore', 'WritingScore']].std(axis=1)
        high_variance = self.df[self.df['ScoreVariance'] > 30]
        if len(high_variance) > 0:
            edge_cases.append({
                'type': 'high_score_variance',
                'description': 'Students with high score variance (> 30)',
                'count': len(high_variance),
                'records': high_variance['StudentID'].tolist()
            })
            logger.warning(f"⚠ Edge case: {len(high_variance)} students with high score variance")
        
        self.edge_cases = edge_cases
        self.validation_results['edge_cases'] = {
            'total_edge_cases': len(edge_cases),
            'edge_cases': edge_cases,
            'passed': len(edge_cases) == 0
        }
        
        return edge_cases
    
    def calculate_quality_metrics(self):
        """
        Calculate overall data quality metrics
        Quality metrics provide quantitative assessment of data health
        """
        logger.info("\n=== QUALITY METRICS CALCULATION ===")
        
        total_records = len(self.df)
        total_cells = total_records * len(self.df.columns)
        
        # Completeness metric
        non_null_cells = total_cells - self.df.isnull().sum().sum()
        completeness = (non_null_cells / total_cells) * 100
        
        # Uniqueness metric (StudentID uniqueness)
        unique_student_ids = self.df['StudentID'].nunique()
        uniqueness = (unique_student_ids / total_records) * 100
        
        # Validity metric (scores in range)
        valid_scores = 0
        total_scores = 0
        for col in ['MathScore', 'ReadingScore', 'WritingScore']:
            valid_scores += len(self.df[(self.df[col] >= 0) & (self.df[col] <= 100)])
            total_scores += len(self.df)
        validity = (valid_scores / total_scores) * 100 if total_scores > 0 else 0
        
        # Consistency metric (categorical values valid)
        consistency_checks = [
            self.df['Gender'].isin(['Male', 'Female']).all(),
            self.df['ParentalEducation'].isin(['High School', 'Some College', "Associate's Degree", 
                                               "Bachelor's Degree", "Master's Degree"]).all(),
            self.df['LunchType'].isin(['Standard', 'Free/Reduced']).all(),
            self.df['TestPreparationCourse'].isin(['Completed', 'None']).all()
        ]
        consistency = (sum(consistency_checks) / len(consistency_checks)) * 100
        
        # Overall quality score
        overall_quality = (completeness + uniqueness + validity + consistency) / 4
        
        quality_metrics = {
            'completeness': round(completeness, 2),
            'uniqueness': round(uniqueness, 2),
            'validity': round(validity, 2),
            'consistency': round(consistency, 2),
            'overall_quality_score': round(overall_quality, 2),
            'total_records': int(total_records),
            'total_cells': int(total_cells),
            'data_quality_grade': self._get_quality_grade(overall_quality)
        }
        
        logger.info(f"Completeness: {completeness:.1f}%")
        logger.info(f"Uniqueness: {uniqueness:.1f}%")
        logger.info(f"Validity: {validity:.1f}%")
        logger.info(f"Consistency: {consistency:.1f}%")
        logger.info(f"Overall Quality Score: {overall_quality:.1f}%")
        logger.info(f"Data Quality Grade: {quality_metrics['data_quality_grade']}")
        
        self.quality_metrics = quality_metrics
        return quality_metrics
    
    def _get_quality_grade(self, score):
        """Convert quality score to grade"""
        if score >= 95:
            return 'A+ (Excellent)'
        elif score >= 90:
            return 'A (Very Good)'
        elif score >= 80:
            return 'B (Good)'
        elif score >= 70:
            return 'C (Acceptable)'
        elif score >= 60:
            return 'D (Poor)'
        else:
            return 'F (Unacceptable)'
    
    def generate_validation_report(self):
        """Generate comprehensive validation report"""
        logger.info("\n=== VALIDATION REPORT GENERATION ===")
        
        report = {
            'validation_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'data_file': self.data_path,
            'total_records': len(self.df),
            'validation_results': self.validation_results,
            'quality_metrics': self.quality_metrics,
            'edge_cases_detected': len(self.edge_cases),
            'edge_cases': self.edge_cases,
            'overall_status': 'PASS' if all([
                self.validation_results.get('score_range_validation', {}).get('passed', True),
                self.validation_results.get('duplicate_detection', {}).get('passed', True),
                self.validation_results.get('null_validation', {}).get('passed', True),
                self.validation_results.get('consistency_validation', {}).get('passed', True)
            ]) else 'FAIL'
        }
        
        return report
    
    def save_validation_report(self, output_path):
        """Save validation report to JSON"""
        report = self.generate_validation_report()
        
        with open(output_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        logger.info(f"Validation report saved to: {output_path}")
        return report
    
    def run_full_validation(self):
        """Run complete validation and quality checks"""
        logger.info("=" * 60)
        logger.info("STUDENT PERFORMANCE DATA VALIDATION & QUALITY CHECKS")
        logger.info("=" * 60)
        
        # Load data
        self.load_data()
        
        # Run all validations
        self.validate_score_ranges()
        self.detect_duplicate_records()
        self.validate_null_values()
        self.validate_data_consistency()
        self.simulate_edge_cases()
        
        # Calculate quality metrics
        self.calculate_quality_metrics()
        
        # Generate report
        report = self.generate_validation_report()
        
        logger.info("\n" + "=" * 60)
        logger.info("VALIDATION COMPLETED")
        logger.info("=" * 60)
        logger.info(f"\nOverall Status: {report['overall_status']}")
        logger.info(f"Quality Score: {self.quality_metrics['overall_quality_score']}%")
        logger.info(f"Quality Grade: {self.quality_metrics['data_quality_grade']}")
        logger.info(f"Edge Cases Detected: {len(self.edge_cases)}")
        
        logger.info(f"\n✓ Ensured reliability through comprehensive validation")
        logger.info(f"✓ Detected {len(self.edge_cases)} anomalies during validation")
        logger.info(f"✓ Data quality grade: {self.quality_metrics['data_quality_grade']}")
        
        return report


def main():
    """Main execution function"""
    data_path = '../data/raw/student_performance.csv'
    output_dir = '../output'
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Initialize validator
    validator = DataValidator(data_path)
    
    # Run validation
    report = validator.run_full_validation()
    
    # Save report
    output_path = os.path.join(output_dir, 'validation_report.json')
    validator.save_validation_report(output_path)
    
    logger.info("\n✓ Data validation completed successfully!")


if __name__ == "__main__":
    main()
