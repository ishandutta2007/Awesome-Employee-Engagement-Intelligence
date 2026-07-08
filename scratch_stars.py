import urllib.request
import json
import re

repos = [
    "BrainStation-23/openofficesurvey",
    "libphoenix/Employee-Engagement-Platform",
    "microsoft/agent-for-hr-service-solution-accelerator",
    "FastAndDanger2/Employee-Sentiment-Analysis",
    "rudrasish2003/Sentiment_Analysis_on_Employee_Feedback",
    "CDAC-lab/employee-review-analysis",
    "sushil79g/Employee_feedback_analysis",
    "zohaibshahzadkhan/EmployeeInsights",
    "kukr/Company-Perception-tool-Using-Sentiment-Analysis",
    "MrBhimani/Employee_Survey_Analysis"
]

stars = {}
for repo in repos:
    try:
        url = f"https://api.github.com/repos/{repo}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            stars[repo] = data.get("stargazers_count", 0)
    except Exception as e:
        print(f"Error fetching {repo}: {e}")
        stars[repo] = 0

print(json.dumps(stars, indent=2))
