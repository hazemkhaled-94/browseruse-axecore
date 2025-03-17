""" Prompt for the Accessibility Audit task. """
from .criteria import Criteria

URL:str = "https://broken-workshop.dequelabs.com/"

criteria_category: str = "PERCEIVABLE" # Change this to Operable, Understandable, or Robust to evaluate the respective criteria.
prompt_text: str = f"""
You are an AI accessibility auditor. Your task is to visit the following URL: {URL}, 
and perform a comprehensive accessibility audit based on the below mentioned WCAG criteria. For each criterion:

1. Scan the website thoroughly.
2. Evaluate the implementation against each of these WCAG Criteria:

3. Ensure that every element on the website is evaluated against each criterion mentioned above.
4. Determine if the criterion has passed, failed, or inapplicable.
5. If the criterion has failed, identify all affected element.
6. For each criteria, provide a brief explanation of the issue.
7. Include all the above mentioned criteria in your report.
8. Ensure that every single criterion listed is evaluated and included in the final report without omissions.
9. Give a percentage of the criteria that passed, failed, and are inapplicable.

Present your findings in a structured format:

## Accessibility Audit Results for https://broken-workshop.dequelabs.com/,

### {criteria_category}

[x.x.x ] [Criteria] [Level]:
- Description: [Issue Description]
- Status: [Passed/Failed/Inapplicable]
- [If Failed] Issue: [Brief explanation]
- [If Failed] Element: [Affected element]

[Continue with all criteria under {criteria_category}]

### Summary

- Total Criteria: [Number]
- Passed: [Number]
- Failed: [Number]
- Inapplicable: [Number]

Provide this comprehensive report, ensuring all WCAG criteria are covered.
"""
