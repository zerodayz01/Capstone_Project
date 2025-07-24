from flask import Flask, request, render_template, jsonify
import requests
import os

app = Flask(__name__, template_folder="templates")

static_folder = os.path.expanduser("~/Desktop/project/static/styles")

app.static_folder = static_folder

base_url = "https://api.data.gov/ed/collegescorecard/v1/"

with open("api_key.txt") as f:
    api_key = f.readline().strip()

fields = [
    
    #Basic Infoormation
    
    "id",
    "school.name",
    "school.city",
    "school.state",
    "latest.admissions.admission_rate.overall",
    "latest.student.size",
    "school.locale",

    #Price and Cost

    "latest.cost.attendance.academic_year",
    "latest.cost.booksupply",
    "latest.cost.tuition.out_of_state",
    "latest.cost.tuition.in_state",
    "latest.cost.roomboard.offcampus",
    "latest.cost.roomboard.oncampus",


    #Price and Cost 2

    "latest.cost.otherexpense.oncampus",
    "latest.cost.otherexpense.offcampus",
    "latest.cost.otherexpense.withfamily",
    "latest.aid.federal_loan_rate",
    "latest.repayment.7_yr_repayment.completers_rate",
    "latest.aid.students_with_any_loan",

    
    #Demos

    "latest.student.demographics.race_ethnicity.white",
    "latest.student.demographics.race_ethnicity.black",
    "latest.student.demographics.race_ethnicity.hispanic",
    "latest.student.demographics.race_ethnicity.asian",
    "latest.student.demographics.race_ethnicity.aian",
    "latest.student.demographics.race_ethnicity.nhpi",
    "latest.student.demographics.race_ethnicity.unknown",


    #Scores

    "latest.admissions.test_requirements",
    "latest.admissions.sat_scores.midpoint.critical_reading",
    "latest.admissions.sat_scores.midpoint.math",
    "latest.admissions.sat_scores.midpoint.writing",
    "latest.admissions.sat_scores.average.overall",
    "latest.admissions.act_scores.midpoint.cumulative",
    "latest.admissions.act_scores.midpoint.english",
    "latest.admissions.act_scores.midpoint.math",
    "latest.admissions.act_scores.midpoint.writing",

    #Contact

    "school.school_url",
    "school.price_calculator_url",
    
    #STEM

    "latest.academics.program.bachelors.biological",
    "latest.academics.pprogram.bachelors.engineering",
    "latest.academics.program.bachelors.computer"
    "latest.academics.program.bachelors.social_science",
    "latest.academics.program.bachelors.mathematics",
    "latest.academics.program.bachelors.physical_science",
    "latest.program.bachelors.architecture",
    
    #Social

    "latest.academics.program.bachelors.communication",
    "latest.academics.pprogram.bachelors.language",
    "latest.academics.program.bachelors.legal"
    "latest.academics.program.bachelors.english",
    "latest.academics.program.bachelors.history",
    "latest.academics.program.bachelors.psychology",
    "latest.program.bachelors.humanities",
    
    #Common/Uncommon

    "latest.academics.program.bachelors.business_marketing",
    "latest.academics.program.bachelors.personal_culinary",
    "latest.academics.program.bachelors.library",
    "latest.academics.program.bachelors.health",
    "latest.academics.program.bachelors.resources",

    #Historic
    
    "school.minority_serving.historically_black",
    "school.minority_serving.tribal",
    "school.men_only",
    "school.women_only",
    "school.religious_affiliation",

    #Metric
    
    "latest.student.share_firstgeneration",
    "latest.student.demographics.age_entry",
    "latest.student.part_time_share",
    "latest.academics.program_reporter.programs_offered",
    
    #Completion

    "latest.student.retention_rate.four_year.full_time",
    "latest.completion.completion_rate_less_than_4yr_150nt",
    "latest.completion.title_iv.completed_by.4yrs",
    
    #Parental Background

    "latest.student.share_firstgeneration_parents.middleschool",
    "latest.student.share_firstgeneration_parents.highschool",
    "latest.student.share_firstgeneration_parents.somecollege",
     
]
options = "&per_page=100&page=0"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def render_index():
    return render_template('index.html')

@app.route('/form.html')
def render_form():
    return render_template('form.html')

@app.route('/resources.html')
def render_resource():
    return render_template('resources.html')

@app.route('/more.html')
def render_more():
    return render_template('more.html')

@app.route('/about.html')
def render_about():
    return render_template('about.html')

@app.route('/contact.html')
def render_contact():
    return render_template('contact.html')

@app.route('/info.html')
def render_info():
    return render_template('info.html')

@app.route('/info2.html')
def render_info2():
    return render_template('info2.html')

@app.route('/demo.html')
def render_demo():
    return render_template('demo.html')

@app.route('/demo2.html')
def render_demo2():
    return render_template('demo2.html')

@app.route('/test.html')
def render_test():
    return render_template('test.html')

@app.route('/load.html')
def render_load():
    return render_template('load.html')

@app.route('/stem.html')
def render_stem():
    return render_template('stem.html')

@app.route('/social.html')
def render_social():
    return render_template('social.html')

@app.route('/other.html')
def render_other():
    return render_template('other.html')

@app.route('/metric.html')
def render_metric():
    return render_template('metric.html')

@app.route('/rate.html')
def render_rate():
    return render_template('rate.html')

@app.route('/back.html')
def render_back():
    return render_template('back.html')

@app.route('/expand.html')
def render_expand():
    return render_template('expand.html')

@app.route('/search', methods=['GET'])
def search_colleges():
    search_query = request.args.get('query', '').lower()

    if search_query == 'umass':
        api_url = f"{base_url}schools.json?{options}&api_key={api_key}&school.name=University of Massachusetts"
        response = requests.get(api_url)

        try:
            response.raise_for_status()
            data = response.json()
            umass_results = data.get('results', [])
            return jsonify({'results': umass_results})

        except requests.exceptions.HTTPError as http_err:
            return jsonify({'error': f"HTTP error occurred: {http_err}"}), 500

        except ValueError as json_err:
            return jsonify({'error': f"JSON decoding error: {json_err}"}), 500

        except requests.exceptions.RequestException as req_err:
            return jsonify({'error': f"Request error occurred: {req_err}"}), 500

        except Exception as err:
            return jsonify({'error': f"An unexpected error occurred: {err}"}), 500

    else:
        api_url = f"{base_url}schools.json?{options}&api_key={api_key}&school.name={search_query}"

        response = requests.get(api_url)

        try:
            response.raise_for_status()
            data = response.json()
            results = data.get('results', [])
            return jsonify({'results': results})

        except requests.exceptions.HTTPError as http_err:
            return jsonify({'error': f"HTTP error occurred: {http_err}"}), 500

        except ValueError as json_err:
            return jsonify({'error': f"JSON decoding error: {json_err}"}), 500

        except requests.exceptions.RequestException as req_err:
            return jsonify({'error': f"Request error occurred: {req_err}"}), 500

        except Exception as err:
            return jsonify({'error': f"An unexpected error occurred: {err}"}), 500

if __name__ == '__main__':
    app.run(port=5001)
