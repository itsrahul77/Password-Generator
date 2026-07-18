# dashboard.py
import datetime
import platform
import sys

def display_dashboard():
    # Get dynamic system info
    now = datetime.datetime.now()
    date_str = now.strftime("%d %B %Y")
    time_str = now.strftime("%I:%M %p")
    py_version = f"{sys.version_info.major}.{sys.version_info.minor}"
    os_name = f"{platform.system()} {platform.release()}"

    # Draw the dashboard
    dashboard = f"""
+----------------------------------------------------------------+
|                          BitXBytes                             |
|                   Cyber Security Toolkit v1.0                  |
+----------------------+-----------------------------------------+
|                      |                                         |
|  Dashboard           |   Welcome to BitXBytes                  |
|  Password Tools      |                                         |
|  Encryption          |   Date : {date_str:<18} |
|  Hashing             |   Time : {time_str:<18} |
|  File Security       |                                         |
|                      |   Python Version : {py_version:<13} |
|                      |   Operating System : {os_name:<11} |
|                      |                                         |
|                      |   Status                                |
|                      |   ✔ Password Tools : Completed          |
|                      |   ⏳ Encryption : Planned               |
|                      |   ⏳ Hashing : Planned                  |
|                      |   ⏳ File Security : Planned            |
|                      |                                         |
+----------------------+-----------------------------------------+
|                    © BitXBytes 2026                            |
+----------------------------------------------------------------+
"""
    print(dashboard)


if __name__ == "__main__":
    display_dashboard()