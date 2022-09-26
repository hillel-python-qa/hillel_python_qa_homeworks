from enum import Enum


class Department(Enum):
    QA_MANUAL = "QA Manual Engineer"
    QA_AUTOMATION = "QA Automation Engineer"
    DEVELOPER_BACK = "Back-end developer"
    DEVELOPER_FRONT = "Front-end developer"
    BA = "Business Analyst"
    PO = "Product Owner"
    TPO = "Technical Product Owner"
    TEAM_LEAD = "Team leader"
    PM = "Project Manager"