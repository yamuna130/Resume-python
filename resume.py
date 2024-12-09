import time
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListItem, ListFlowable, HRFlowable

def intro():
    print("Welcome to the Python Resume Builder!\n")
    time.sleep(1)
    print("Let's build your professional fresher resume.\n")
    time.sleep(1)

def get_input(prompt, is_numeric=False, optional=False):
    while True:
        user_input = input(prompt + ": ")
        if not user_input and optional:  # Allow empty input if it's optional
            return ""
        if is_numeric:
            try:
                return int(user_input)
            except ValueError:
                print("Please enter a valid number.")
        else:
            if user_input:
                return user_input
            else:
                print("This field cannot be empty. Please enter a valid input.")

def build_resume():
    intro()
    
    # Get user details
    name = get_input("Enter your full name")
    email = get_input("Enter your email address")
    phone = get_input("Enter your phone number")
    linkedin = get_input("Enter your LinkedIn profile link (optional)", optional=True)
    github = get_input("Enter your GitHub link (optional)", optional=True)
    objective = get_input("Enter your career objective or summary")
    skills = get_input("Enter your skills (comma separated)")
    education = get_input("Enter your highest education (e.g., B.Tech in Computer Science)")

    # Multiple Projects Section
    projects = []
    project_count = get_input("How many projects would you like to add?", is_numeric=True)
    for i in range(project_count):
        project_title = get_input(f"Enter title for Project {i + 1}")
        project_description = get_input(f"Enter description for Project '{project_title}'")
        projects.append((project_title, project_description))

    # Multiple Internship Experiences
    internships = []
    internship_count = get_input("How many internship experiences would you like to add? (optional, 0 for none)", is_numeric=True)
    for i in range(internship_count):
        company = get_input(f"Enter company name for Internship {i + 1}")
        internship_role = get_input(f"Enter your role at {company}")
        internship_desc = get_input(f"Enter description for Internship at {company}")
        internships.append((company, internship_role, internship_desc))
    
    # Multiple Work Experiences (Jobs)
    work_experience = []
    job_count = get_input("How many job experiences would you like to add? (optional, 0 for none)", is_numeric=True)
    for i in range(job_count):
        company = get_input(f"Enter company name for Job {i + 1}")
        job_role = get_input(f"Enter your role at {company}")
        job_desc = get_input(f"Enter description for Job at {company}")
        work_experience.append((company, job_role, job_desc))

    # Certifications Section
    certifications = []
    cert_count = get_input("How many certifications do you want to add? (optional, 0 for none)", is_numeric=True)
    for i in range(cert_count):
        cert = get_input(f"Enter Certification {i + 1} details (e.g., 'Certified Python Developer')")
        certifications.append(cert)

    # Constructing the Resume content
    content = []

    # Header - Name and Contact Info
    content.append(Paragraph(f"<font size=18 color={colors.darkblue}><b>{name}</b></font>", getSampleStyleSheet()['Heading1']))
    content.append(Spacer(1, 6))
    content.append(Paragraph(f"<font size=12 color={colors.black}><b>Email:</b> {email} | <b>Phone:</b> {phone}</font>", getSampleStyleSheet()['Normal']))
    if linkedin:
        content.append(Paragraph(f"<font size=12 color={colors.blue}>LinkedIn: {linkedin}</font>", getSampleStyleSheet()['Normal']))
    if github:
        content.append(Paragraph(f"<font size=12 color={colors.green}>GitHub: {github}</font>", getSampleStyleSheet()['Normal']))
    content.append(Spacer(1, 12))

    # Horizontal line above Objective
    content.append(HRFlowable(width="100%", thickness=1, color=colors.black, spaceBefore=12, spaceAfter=12))

    # Objective Section
    content.append(Paragraph(f"<font size=14 color={colors.darkblue}><b>OBJECTIVE</b></font>", ParagraphStyle(name='Heading2', fontSize=14, textColor=colors.darkblue, alignment=0)))
    content.append(Spacer(1, 6))
    content.append(Paragraph(objective, getSampleStyleSheet()['Normal']))
    content.append(Spacer(1, 12))

    # Skills Section (bulleted points)
    content.append(Paragraph(f"<font size=14 color={colors.darkblue}><b>SKILLS</b></font>", ParagraphStyle(name='Heading2', fontSize=14, textColor=colors.darkblue, alignment=0)))
    content.append(Spacer(1, 6))
    skill_list = skills.split(",")
    skill_points = [ListItem(Paragraph(f"<font size=12>{skill.strip()}</font>", getSampleStyleSheet()['Normal'])) for skill in skill_list]
    skills_list = ListFlowable(skill_points, bulletType='bullet', bulletFontSize=12, spaceBefore=6)
    content.append(skills_list)
    content.append(Spacer(1, 12))

    # Education Section
    content.append(Paragraph(f"<font size=14 color={colors.darkblue}><b>EDUCATION</b></font>", ParagraphStyle(name='Heading2', fontSize=14, textColor=colors.darkblue, alignment=0)))
    content.append(Spacer(1, 6))
    content.append(Paragraph(f"<font size=12>{education}</font>", getSampleStyleSheet()['Normal']))
    content.append(Spacer(1, 12))

    # Projects Section (multiple projects)
    content.append(Paragraph(f"<font size=14 color={colors.darkblue}><b>PROJECTS</b></font>", ParagraphStyle(name='Heading2', fontSize=14, textColor=colors.darkblue, alignment=0)))
    content.append(Spacer(1, 6))
    for i, (title, description) in enumerate(projects):
        content.append(Paragraph(f"<font size=12><b>{title}:</b> {description}</font>", getSampleStyleSheet()['Normal']))
        content.append(Spacer(1, 6))
    content.append(Spacer(1, 12))

    # Internships Section (multiple internships)
    if internships:
        content.append(Paragraph(f"<font size=14 color={colors.darkblue}><b>INTERNSHIPS</b></font>", ParagraphStyle(name='Heading2', fontSize=14, textColor=colors.darkblue, alignment=0)))
        content.append(Spacer(1, 6))
        for i, (company, role, internship) in enumerate(internships):
            content.append(Paragraph(f"<font size=12><b>{company} ({role}):</b></font>", getSampleStyleSheet()['Normal']))
            internship_list = internship.split("\n")
            internship_points = [ListItem(Paragraph(f"<font size=12>{point.strip()}</font>", getSampleStyleSheet()['Normal'])) for point in internship_list]
            internship_list_flowable = ListFlowable(internship_points, bulletType='bullet', bulletFontSize=12, spaceBefore=6)
            content.append(internship_list_flowable)
            content.append(Spacer(1, 6))
        content.append(Spacer(1, 12))

    # Work Experience Section (multiple jobs)
    if work_experience:
        content.append(Paragraph(f"<font size=14 color={colors.darkblue}><b>WORK EXPERIENCE</b></font>", ParagraphStyle(name='Heading2', fontSize=14, textColor=colors.darkblue, alignment=0)))
        content.append(Spacer(1, 6))
        for i, (company, role, job) in enumerate(work_experience):
            content.append(Paragraph(f"<font size=12><b>{company} ({role}):</b></font>", getSampleStyleSheet()['Normal']))
            job_list = job.split("\n")
            job_points = [ListItem(Paragraph(f"<font size=12>{point.strip()}</font>", getSampleStyleSheet()['Normal'])) for point in job_list]
            job_list_flowable = ListFlowable(job_points, bulletType='bullet', bulletFontSize=12, spaceBefore=6)
            content.append(job_list_flowable)
            content.append(Spacer(1, 6))
        content.append(Spacer(1, 12))

    # Certifications Section (multiple certifications in bulleted points)
    if certifications:
        content.append(Paragraph(f"<font size=14 color={colors.darkblue}><b>CERTIFICATIONS</b></font>", ParagraphStyle(name='Heading2', fontSize=14, textColor=colors.darkblue, alignment=0)))
        content.append(Spacer(1, 6))
        certification_points = [ListItem(Paragraph(f"<font size=12>{cert}</font>", getSampleStyleSheet()['Normal'])) for cert in certifications]
        certifications_list = ListFlowable(certification_points, bulletType='bullet', bulletFontSize=12, spaceBefore=6)
        content.append(certifications_list)
        content.append(Spacer(1, 12))

    # Saving as PDF
    pdf_filename = f"{name}_fresher_resume.pdf"
    resume = SimpleDocTemplate(pdf_filename, pagesize=letter)
    resume.build(content)
    
    print(f"\nYour resume has been successfully created and saved as {pdf_filename}!")

if __name__ == "__main__":
    build_resume()

