import streamlit as st

header = st.container()
box1 = st.container()
box2 = st.container()
box3 = st.container()
box4 = st.container()
result = st.container()

corpus = "LMS"
tasks_ID = ["SYL", "WOR", "PAS", "SNO", "SFA", "SCL"]
participants_ID = [
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
]
participants_Gender = ["F", "M", "N"]
sessions_ID = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8"]

with header:
    st.title("LMS Naming Tool")
    st.markdown(
        "This mini-app generates the base file name for the LMS Project. &nbsp;"
        "[![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/patricia-ternes/LMS_naming_tool)"
    )
    st.markdown("***")

with box1:
    task_ID = st.selectbox("Task ID:", tasks_ID, label_visibility="visible")

with box2:
    participant_ID = st.selectbox(
        "Participant ID:", participants_ID, label_visibility="visible"
    )

with box3:
    participant_Gender = st.selectbox(
        "Participant Gender:", participants_Gender, label_visibility="visible"
    )

with box4:
    session_ID = st.selectbox("session ID:", sessions_ID, label_visibility="visible")
    st.markdown("***")

with result:
    st.markdown("### The file name is:")
    file_name = "_".join(
        [corpus, task_ID, participant_ID, participant_Gender, session_ID]
    )
    st.code(file_name, language="bash")
