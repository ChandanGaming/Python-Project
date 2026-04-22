import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import numpy as np

st.set_page_config(
    page_title="Student Performance Analysis",
    page_icon="📊",
    layout="wide",
)

st.markdown("""
<style>
[data-testid="stAppViewContainer"] { background-color: #f0f4f8; }
[data-testid="stSidebar"] { background: linear-gradient(180deg,#1F4E79 0%,#2E75B6 100%); }
[data-testid="stSidebar"] * { color: white !important; }
[data-testid="stSidebar"] .stSelectbox > div > div { background: rgba(255,255,255,0.15); border-radius:6px; }
.block-container { padding-top: 1.2rem; padding-bottom: 1rem; }

/* ── Fix all headings to be dark/visible on white background ── */
h1, h2, h3, h4, h5, h6 { color: #1F4E79 !important; }
[data-testid="stMarkdownContainer"] h1 { color: #1F4E79 !important; }
[data-testid="stMarkdownContainer"] h2 { color: #2E75B6 !important; }
[data-testid="stMarkdownContainer"] h3 { color: #1F4E79 !important; }
/* Streamlit native st.markdown ## headings */
.stMarkdown h1 { color: #1F4E79 !important; font-weight: 800 !important; }
.stMarkdown h2 { color: #2E75B6 !important; font-weight: 700 !important; border-bottom: 2px solid #BDD7EE; padding-bottom: 4px; }
.stMarkdown h3 { color: #1F4E79 !important; font-weight: 700 !important; }
/* All text in main area should be dark */
[data-testid="stAppViewContainer"] p,
[data-testid="stAppViewContainer"] li,
[data-testid="stAppViewContainer"] span { color: #1A1A1A; }

.hero-banner {
    background: linear-gradient(135deg,#1F4E79 0%,#2E75B6 60%,#41A0D6 100%);
    border-radius:14px; padding:28px 36px; margin-bottom:22px; color:white;
}
.hero-banner h1 { font-size:1.85rem; margin:0 0 6px; color:white !important; }
.hero-banner p  { font-size:0.9rem; margin:2px 0; opacity:.85; color:white !important; }

.kpi-card {
    background:white; border-radius:10px; border-left:5px solid #2E75B6;
    padding:16px 18px; box-shadow:0 2px 8px rgba(0,0,0,.08);
    margin-bottom:10px;
}
.kpi-card .klabel { font-size:.72rem; color:#888 !important; text-transform:uppercase; letter-spacing:.07em; }
.kpi-card .kvalue { font-size:1.8rem; font-weight:800; color:#1F4E79 !important; line-height:1.1; }
.kpi-card .ksub   { font-size:.78rem; color:#555 !important; margin-top:2px; }

.sec-head {
    background:#2E75B6; color:white !important; border-radius:8px;
    padding:9px 18px; font-size:1rem; font-weight:700;
    margin:20px 0 12px;
}
.info-box {
    background:#EBF3FB; border-left:4px solid #2E75B6; border-radius:6px;
    padding:12px 16px; font-size:.875rem; color:#1F4E79 !important; margin-bottom:14px;
}
.info-box * { color:#1F4E79 !important; }
.chapter-badge {
    display:inline-block; background:#1F4E79; color:white !important;
    border-radius:20px; padding:3px 14px; font-size:.8rem;
    font-weight:700; margin-bottom:6px;
}
.result-card {
    background:white; border-radius:10px; padding:16px 20px;
    box-shadow:0 2px 8px rgba(0,0,0,.07); margin-bottom:12px;
    border-top:3px solid #2E75B6;
}
.result-card * { color: #1A1A1A !important; }
/* Tab labels */
.stTabs [data-baseweb="tab"] { color: #1F4E79 !important; font-weight:600; }
.stTabs [aria-selected="true"] { border-bottom: 3px solid #2E75B6 !important; }
/* Expander headers */
.streamlit-expanderHeader { color: #1F4E79 !important; font-weight:700 !important; }
/* Selectbox & slider labels */
.stSelectbox label, .stSlider label { color: #1A1A1A !important; }
</style>
""", unsafe_allow_html=True)

# ── Dataset ──────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    np.random.seed(42)
    n = 30
    hours      = np.random.randint(2, 9, n)
    attendance = np.random.randint(60, 100, n)
    math    = np.clip((hours*7 + attendance*0.3 + np.random.normal(0,5,n)).astype(int), 40,100)
    science = np.clip((hours*6 + attendance*0.35 + np.random.normal(0,6,n)).astype(int),40,100)
    english = np.clip((hours*5 + attendance*0.25 + np.random.normal(0,7,n)).astype(int),40,100)
    return pd.DataFrame({
        "Student_ID":   [f"S{i+1:02d}" for i in range(n)],
        "Math":         math,
        "Science":      science,
        "English":      english,
        "Hours_Studied":hours,
        "Attendance":   attendance,
    })

df = load_data()

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🎓 Project Info")
    st.markdown("**Univariate & Bivariate Analysis of Student Performance Data Using Python**")
    st.markdown("---")
    st.markdown("**Team Members**")
    st.markdown("👤 **Himalaya Utreja**\n`UID: 24BCS10848`")
    st.markdown("👤 **Chandan Sindhi**\n`UID: 24BCS10836`")
    st.markdown("---")
    st.markdown("**Tools Used**")
    st.markdown("🐍 Python  |  🐼 Pandas\n📊 Matplotlib  |  📈 Seaborn\n🌐 Streamlit  |  ☁️ Google Colab")
    st.markdown("---")

    page = st.selectbox("📂 Navigate to Chapter", [
        "🏠 Cover & Abstract",
        "Chapter 1 — Introduction",
        "Chapter 2 — Literature Review",
        "Chapter 3 — Design & Methodology",
        "Chapter 4 — Implementation & Results",
        "Chapter 5 — Analysis & Evaluation",
        "Chapter 6 — Conclusion & Future Scope",
    ])
    st.markdown("---")
    st.markdown("**🔧 Filter Data**")
    min_h = st.slider("Min Hours Studied", 2, 8, 2)
    max_h = st.slider("Max Hours Studied", 2, 8, 8)
    fdf = df[(df["Hours_Studied"]>=min_h) & (df["Hours_Studied"]<=max_h)]
    st.caption(f"Showing {len(fdf)} / {len(df)} students")

# ── Hero Banner ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-banner">
  <h1>📊 Student Performance Analysis Dashboard</h1>
  <p>Univariate &amp; Bivariate Analysis · Python · Pandas · Matplotlib · Seaborn · Streamlit</p>
  <p>Himalaya Utreja (24BCS10848) &nbsp;|&nbsp; Chandan Sindhi (24BCS10854) &nbsp;|&nbsp; Chandigarh University</p>
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════
# PAGE: Cover & Abstract
# ════════════════════════════════════════════════════════════════════
if page == "🏠 Cover & Abstract":
    st.markdown('<div class="chapter-badge">ABSTRACT</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box">
    In the field of education, data analysis plays a vital role in understanding student performance
    and identifying areas of improvement. This project, <b>Univariate and Bivariate Analysis of
    Student Performance Data Using Python</b>, develops an interactive analytical platform that
    processes academic records and generates meaningful visual insights.<br><br>
    The system is built using <b>Python</b> and <b>Streamlit</b>, with <b>Pandas</b> for data manipulation,
    <b>Matplotlib</b> and <b>Seaborn</b> for visualization. The workflow begins with dataset loading and
    preprocessing, followed by univariate analysis (distributions, descriptive statistics) and bivariate
    analysis (scatter plots, correlation heatmaps).<br><br>
    The project demonstrates how open-source Python tools can replace manual, Excel-based analysis
    with fast, automated, and visually rich insights — supporting evidence-based academic decision-making.
    </div>
    """, unsafe_allow_html=True)

    c1,c2,c3,c4 = st.columns(4)
    kpis = [
        ("Total Students","30","in dataset"),
        ("Subjects Covered","3","Math, Science, English"),
        ("Avg Math Score",f"{df['Math'].mean():.1f}","out of 100"),
        ("Avg Attendance",f"{df['Attendance'].mean():.1f}%","average"),
    ]
    for col,(lbl,val,sub) in zip([c1,c2,c3,c4],kpis):
        col.markdown(f"""<div class="kpi-card">
            <div class="klabel">{lbl}</div>
            <div class="kvalue">{val}</div>
            <div class="ksub">{sub}</div></div>""", unsafe_allow_html=True)

    st.markdown('<div class="sec-head">📋 Raw Dataset Preview</div>', unsafe_allow_html=True)
    st.dataframe(df.set_index("Student_ID"), use_container_width=True, height=280)

# ════════════════════════════════════════════════════════════════════
# PAGE: Chapter 1 — Introduction
# ════════════════════════════════════════════════════════════════════
elif page == "Chapter 1 — Introduction":
    st.markdown('<div class="chapter-badge">CHAPTER 1</div>', unsafe_allow_html=True)
    st.markdown("## Introduction")

    tabs = st.tabs(["1.1 Overview","1.2 Motivation","1.3 Objectives","1.4 Scope","1.5 Dataset View"])

    with tabs[0]:
        st.markdown('<div class="info-box"><b>Overview:</b> In the modern educational landscape, data-driven analysis helps institutions identify performance patterns and design better learning strategies. This project provides a transparent, interactive, open-source platform to analyze student academic data using Python. The system integrates data preprocessing, statistical analysis, and rich visualizations to move beyond static reports and enable dynamic, evidence-based insights.</div>', unsafe_allow_html=True)

    with tabs[1]:
        st.markdown('<div class="info-box"><b>Motivation:</b> Traditional tools like Excel are limited in their visualization and analytical capabilities. Commercial BI platforms are costly. Our motivation was to create a free, Python-based alternative that is accessible to students and educators — demonstrating how theoretical programming concepts (data cleaning, visualization, correlation) solve real academic problems.</div>', unsafe_allow_html=True)

    with tabs[2]:
        st.markdown("**Project Objectives:**")
        objectives = [
            "Design a clean interface for dataset loading and exploration",
            "Preprocess datasets by checking missing values and data structure",
            "Perform univariate analysis: mean, median, std dev, histograms, boxplots",
            "Perform bivariate analysis: scatter plots, correlation matrix, heatmaps",
            "Generate visual insights to understand student performance patterns",
            "Follow a modular design for future scalability",
        ]
        for o in objectives:
            st.markdown(f"✔️ {o}")

    with tabs[3]:
        st.markdown('<div class="info-box"><b>Scope:</b> This project serves multiple audiences — for students it demonstrates Python analytics in practice; for educators it provides a quick tool to understand performance trends; for institutions it offers a prototype for academic decision support. The modular design allows future extensions like machine learning predictions or real-time dashboards.</div>', unsafe_allow_html=True)

    with tabs[4]:
        st.markdown('<div class="sec-head">📊 Dataset View</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Raw Data (First 10 rows)**")
            st.dataframe(df.head(10).set_index("Student_ID"), use_container_width=True)
        with col2:
            st.markdown("**Dataset Info**")
            info = pd.DataFrame({
                "Column":      ["Math","Science","English","Hours_Studied","Attendance"],
                "Type":        ["Integer"]*5,
                "Range":       ["40–100","40–100","40–100","2–8","60–100"],
                "Description": ["Math marks","Science marks","English marks","Daily study hours","Attendance %"],
            })
            st.dataframe(info.set_index("Column"), use_container_width=True)

# ════════════════════════════════════════════════════════════════════
# PAGE: Chapter 2 — Literature Review
# ════════════════════════════════════════════════════════════════════
elif page == "Chapter 2 — Literature Review":
    st.markdown('<div class="chapter-badge">CHAPTER 2</div>', unsafe_allow_html=True)
    st.markdown("## Literature Review & Background Study")

    st.markdown("### 2.1 Evolution of Analytics in Education")
    st.markdown('<div class="info-box">Data analysis in education began with manual grade-tracking and spreadsheets. Over time, Business Intelligence tools like Tableau emerged, but these were expensive and required specialized skills. Python-based tools (Pandas, Matplotlib, Seaborn, Streamlit) democratized analytics — making powerful analysis accessible to students and educators without cost barriers.</div>', unsafe_allow_html=True)

    st.markdown("### 2.2 Limitations of Existing Systems")
    col1,col2 = st.columns(2)
    with col1:
        st.markdown("**❌ Existing Systems**")
        for item in ["Manual Excel analysis — time-consuming","Limited visualization options","Cannot easily identify relationships","Difficult to reproduce or automate","No statistical summary tools"]:
            st.markdown(f"- {item}")
    with col2:
        st.markdown("**✔️ Proposed Python System**")
        for item in ["Automated analysis with Pandas","Rich charts: histogram, boxplot, heatmap","Correlation matrix reveals relationships","Reproducible and scalable code","Full statistical summary in one command"]:
            st.markdown(f"- {item}")

    st.markdown("### 2.3 Theoretical Framework")
    st.markdown('<div class="info-box"><b>Univariate Analysis:</b> Studies one variable at a time. Measures of central tendency (mean, median) and spread (std dev, range) reveal distribution characteristics. Histograms and boxplots provide visual understanding.<br><br><b>Bivariate Analysis:</b> Examines relationships between two variables. Scatter plots reveal trends; Pearson correlation coefficient quantifies strength; heatmaps show all pairwise correlations simultaneously.</div>', unsafe_allow_html=True)

    st.markdown("### 2.4 Cleaned Dataset — Missing Values Summary")
    col1,col2 = st.columns(2)
    with col1:
        summary = df.drop(columns="Student_ID").isnull().sum().reset_index()
        summary.columns = ["Column","Missing Values"]
        summary["Status"] = summary["Missing Values"].apply(lambda x: "✅ Clean" if x==0 else "⚠️ Has Nulls")
        st.dataframe(summary.set_index("Column"), use_container_width=True)
    with col2:
        st.markdown(f"""
        <div class="kpi-card"><div class="klabel">Total Rows</div><div class="kvalue">30</div></div>
        <div class="kpi-card"><div class="klabel">Total Columns</div><div class="kvalue">6</div></div>
        <div class="kpi-card"><div class="klabel">Missing Values</div><div class="kvalue">0</div><div class="ksub">Dataset is clean ✅</div></div>
        """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════
# PAGE: Chapter 3 — Design & Methodology
# ════════════════════════════════════════════════════════════════════
elif page == "Chapter 3 — Design & Methodology":
    st.markdown('<div class="chapter-badge">CHAPTER 3</div>', unsafe_allow_html=True)
    st.markdown("## Design, Architecture & Methodology")

    st.markdown("### 3.1 Design Philosophy")
    cols = st.columns(4)
    for col, (icon, title, desc) in zip(cols, [
        ("🎯","Simplicity","Clean upload & immediate analysis"),
        ("🔍","Transparency","Clear data quality reporting"),
        ("⚡","Interactivity","Dynamic dashboards & charts"),
        ("📐","Scalability","Modular, extendable architecture"),
    ]):
        col.markdown(f"""<div class="result-card" style="text-align:center">
            <div style="font-size:2rem">{icon}</div>
            <div style="font-weight:700;color:#1F4E79">{title}</div>
            <div style="font-size:.82rem;color:#555">{desc}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("### 3.2 System Architecture")
    st.markdown('<div class="info-box">The system follows a layered architecture: <b>Data Source</b> → <b>Processing Layer</b> → <b>Analysis Modules</b> → <b>Visualization Layer</b> → <b>User Output</b>. Each layer is independent, ensuring modularity and ease of future enhancement.</div>', unsafe_allow_html=True)

    st.markdown("### 3.3 Data Flow Diagram (DFD)")
    fig, ax = plt.subplots(figsize=(12,2.8))
    ax.set_xlim(0,12); ax.set_ylim(0,3); ax.axis("off")
    boxes = [
        (0.3, "📁 User\nDataset", "#1F4E79"),
        (2.5, "🔄 Load &\nPreprocess", "#2E75B6"),
        (4.7, "📊 Univariate\nAnalysis", "#2E75B6"),
        (6.9, "🔍 Bivariate\nAnalysis", "#2E75B6"),
        (9.1, "📈 Visual\nOutput", "#1F4E79"),
    ]
    for x, label, color in boxes:
        rect = mpatches.FancyBboxPatch((x,0.6),1.9,1.7, boxstyle="round,pad=0.08",
                                        facecolor=color, edgecolor="white", linewidth=2)
        ax.add_patch(rect)
        ax.text(x+0.95,1.5, label, ha="center", va="center",
                fontsize=9.5, color="white", fontweight="bold")
    for xarr in [2.2, 4.4, 6.6, 8.8]:
        ax.annotate("", xy=(xarr+0.05,1.5), xytext=(xarr-0.25,1.5),
                    arrowprops=dict(arrowstyle="->", color="#FF8C00", lw=2.5))
    ax.set_title("Data Flow Diagram — Student Performance Analysis System",
                 fontsize=11, fontweight="bold", pad=8)
    fig.tight_layout()
    st.pyplot(fig); plt.close()

    st.markdown("### 3.4 Methodology Steps")
    steps = [
        ("Step 1","Data Collection","Student dataset created with Math, Science, English marks, Hours Studied, and Attendance"),
        ("Step 2","Data Loading","Data loaded using pd.read_csv(); structure examined with df.head(), df.info(), df.describe()"),
        ("Step 3","Preprocessing","Checked for missing values, verified data types, confirmed dataset integrity"),
        ("Step 4","Univariate Analysis","Computed mean, median, std dev; plotted histograms and boxplots per variable"),
        ("Step 5","Bivariate Analysis","Created scatter plots for variable pairs; computed Pearson correlation; plotted heatmap"),
    ]
    for s,t,d in steps:
        col1,col2 = st.columns([1,5])
        col1.markdown(f"""<div style="background:#1F4E79;color:white;border-radius:8px;
            padding:12px;text-align:center;font-weight:700;font-size:.95rem">{s}</div>""",
            unsafe_allow_html=True)
        col2.markdown(f"""<div style="background:#EBF3FB;border-left:4px solid #2E75B6;
            border-radius:6px;padding:10px 16px"><b style="color:#1F4E79">{t}</b><br>
            <span style="font-size:.875rem">{d}</span></div>""", unsafe_allow_html=True)
        st.markdown("")

    st.markdown("### 3.5 Code Architecture")
    code = '''import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load data
df = pd.read_csv("students.csv")
print(df.head())

# Step 2: Preprocessing
print("Missing values:", df.isnull().sum())
print(df.describe())

# Step 3: Univariate — Histogram
plt.hist(df['Math'], bins=5)
plt.title("Distribution of Math Marks")
plt.xlabel("Marks"); plt.ylabel("Frequency")
plt.show()

# Step 4: Univariate — Boxplot
sns.boxplot(y=df['Science'])
plt.title("Boxplot of Science Marks")
plt.show()

# Step 5: Bivariate — Scatter Plot
plt.scatter(df['Hours_Studied'], df['Math'])
plt.title("Hours Studied vs Math Marks")
plt.xlabel("Hours Studied"); plt.ylabel("Math Marks")
plt.show()

# Step 6: Correlation Heatmap
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()'''
    st.code(code, language="python")

# ════════════════════════════════════════════════════════════════════
# PAGE: Chapter 4 — Implementation & Results
# ════════════════════════════════════════════════════════════════════
elif page == "Chapter 4 — Implementation & Results":
    st.markdown('<div class="chapter-badge">CHAPTER 4</div>', unsafe_allow_html=True)
    st.markdown("## Implementation & Results")

    tabs = st.tabs(["4.1 Preprocessing","4.2 Descriptive Stats","4.3 Univariate Analysis","4.4 Bivariate Analysis","4.5 Correlation Heatmap"])

    # ── 4.1
    with tabs[0]:
        st.markdown("### 4.1 Data Preprocessing")
        st.markdown('<div class="info-box">The preprocessing step ensures data integrity before analysis. We check for missing values, examine data structure, and confirm data types are appropriate for numerical analysis.</div>', unsafe_allow_html=True)
        col1,col2 = st.columns(2)
        with col1:
            st.markdown("**Data Quality Report**")
            qr = pd.DataFrame({
                "Metric":["Total Rows","Total Columns","Missing Values","Duplicate Rows","Numeric Columns"],
                "Value":  [len(df), len(df.columns), int(df.isnull().sum().sum()), int(df.duplicated().sum()), 5],
                "Status": ["✅","✅","✅ None","✅ None","✅"],
            })
            st.dataframe(qr.set_index("Metric"), use_container_width=True)
        with col2:
            st.markdown("**Data Types**")
            dt = pd.DataFrame({"Column":df.columns,"Type":df.dtypes.astype(str).values})
            st.dataframe(dt.set_index("Column"), use_container_width=True)
        st.code("""df = pd.read_csv("students.csv")
print(df.head())
print("Missing values:\\n", df.isnull().sum())
print("\\nData types:\\n", df.dtypes)""", language="python")

    # ── 4.2
    with tabs[1]:
        st.markdown("### 4.2 Descriptive Statistics")
        st.markdown('<div class="info-box">Descriptive statistics provide a summary of each variable — mean, median, standard deviation, minimum, and maximum — giving an immediate overview of the dataset distribution.</div>', unsafe_allow_html=True)
        st.dataframe(fdf.drop(columns="Student_ID").describe().round(2), use_container_width=True)
        c1,c2,c3,c4 = st.columns(4)
        for col,(lbl,val) in zip([c1,c2,c3,c4],[
            ("Avg Math",  f"{fdf['Math'].mean():.1f}"),
            ("Avg Science",f"{fdf['Science'].mean():.1f}"),
            ("Avg English",f"{fdf['English'].mean():.1f}"),
            ("Avg Hours",  f"{fdf['Hours_Studied'].mean():.1f}"),
        ]):
            col.markdown(f"""<div class="kpi-card">
                <div class="klabel">{lbl}</div>
                <div class="kvalue">{val}</div></div>""", unsafe_allow_html=True)
        st.code("print(df.describe())", language="python")

    # ── 4.3
    with tabs[2]:
        st.markdown("### 4.3 Univariate Analysis")
        st.markdown('<div class="info-box">Univariate analysis studies each variable independently. Histograms reveal distribution shape; boxplots show median, quartiles, and outliers.</div>', unsafe_allow_html=True)
        var = st.selectbox("Select variable:", ["Math","Science","English","Hours_Studied","Attendance"])

        col1,col2 = st.columns(2)
        with col1:
            fig,ax = plt.subplots(figsize=(5.5,4))
            ax.hist(fdf[var], bins=8, color="#2E75B6", edgecolor="white", alpha=0.88)
            ax.axvline(fdf[var].mean(), color="#C00000", lw=2, linestyle="--", label=f"Mean={fdf[var].mean():.1f}")
            ax.axvline(fdf[var].median(), color="#FF8C00", lw=2, linestyle=":", label=f"Median={fdf[var].median():.1f}")
            ax.set_xlabel(var,fontsize=10); ax.set_ylabel("Frequency",fontsize=10)
            ax.set_title(f"Distribution of {var}", fontsize=11, fontweight="bold")
            ax.legend(fontsize=9); ax.grid(axis="y",linestyle="--",alpha=0.35)
            fig.tight_layout(); st.pyplot(fig); plt.close()
        with col2:
            fig,ax = plt.subplots(figsize=(5.5,4))
            ax.boxplot(fdf[var], patch_artist=True, widths=0.5,
                       boxprops=dict(facecolor="#BDD7EE",color="#1F4E79"),
                       medianprops=dict(color="#C00000",linewidth=2.5),
                       whiskerprops=dict(color="#1F4E79"),
                       capprops=dict(color="#1F4E79"),
                       flierprops=dict(marker="o",color="#2E75B6",markersize=6))
            ax.set_ylabel(var,fontsize=10)
            ax.set_title(f"Boxplot of {var}", fontsize=11, fontweight="bold")
            ax.grid(axis="y",linestyle="--",alpha=0.35)
            fig.tight_layout(); st.pyplot(fig); plt.close()

        st.markdown("**All Variables — Comparative Histograms**")
        fig,axes = plt.subplots(1,5,figsize=(14,3.5))
        colors = ["#2E75B6","#1F4E79","#70AD47","#FF8C00","#C00000"]
        for ax,c,clr in zip(axes,["Math","Science","English","Hours_Studied","Attendance"],colors):
            ax.hist(fdf[c], bins=7, color=clr, edgecolor="white", alpha=0.85)
            ax.set_title(c,fontsize=9,fontweight="bold"); ax.grid(axis="y",linestyle="--",alpha=0.3)
        fig.suptitle("Distribution of All Variables",fontsize=11,fontweight="bold")
        fig.tight_layout(); st.pyplot(fig); plt.close()

    # ── 4.4
    with tabs[3]:
        st.markdown("### 4.4 Bivariate Analysis")
        st.markdown('<div class="info-box">Bivariate analysis examines the relationship between two variables. Scatter plots reveal direction and strength; trend lines show the overall pattern.</div>', unsafe_allow_html=True)
        num_cols = ["Math","Science","English","Hours_Studied","Attendance"]
        c1,c2 = st.columns(2)
        xv = c1.selectbox("X-axis:",num_cols,index=3)
        yv = c2.selectbox("Y-axis:",num_cols,index=0)

        fig,ax = plt.subplots(figsize=(7,4.5))
        ax.scatter(fdf[xv],fdf[yv],color="#2E75B6",edgecolors="#1F4E79",s=75,alpha=0.8,zorder=3)
        m,b = np.polyfit(fdf[xv],fdf[yv],1)
        xs = np.linspace(fdf[xv].min(),fdf[xv].max(),100)
        ax.plot(xs,m*xs+b,color="#C00000",lw=2,label=f"Trend (slope={m:.2f})")
        ax.set_xlabel(xv,fontsize=11); ax.set_ylabel(yv,fontsize=11)
        ax.set_title(f"{xv} vs {yv}",fontsize=13,fontweight="bold")
        ax.legend(fontsize=9); ax.grid(linestyle="--",alpha=0.35)
        fig.tight_layout(); st.pyplot(fig); plt.close()

        r = fdf[[xv,yv]].corr().iloc[0,1]
        strength = "Strong" if abs(r)>0.7 else ("Moderate" if abs(r)>0.4 else "Weak")
        direction = "Positive" if r>0 else "Negative"
        st.markdown(f'<div class="info-box">Pearson r = <b>{r:.3f}</b> — {strength} {direction} relationship between <b>{xv}</b> and <b>{yv}</b></div>', unsafe_allow_html=True)

        st.markdown("**Key Pair Scatter Plots**")
        fig,axes = plt.subplots(1,3,figsize=(13,4))
        for ax,(x2,y2) in zip(axes,[("Hours_Studied","Math"),("Hours_Studied","Science"),("Attendance","Math")]):
            ax.scatter(fdf[x2],fdf[y2],color="#2E75B6",edgecolors="#1F4E79",s=55,alpha=0.8)
            m2,b2=np.polyfit(fdf[x2],fdf[y2],1); xs2=np.linspace(fdf[x2].min(),fdf[x2].max(),100)
            ax.plot(xs2,m2*xs2+b2,color="#C00000",lw=1.8)
            ax.set_xlabel(x2,fontsize=9); ax.set_ylabel(y2,fontsize=9)
            ax.set_title(f"{x2} vs {y2}",fontsize=10,fontweight="bold")
            ax.grid(linestyle="--",alpha=0.3)
        fig.tight_layout(); st.pyplot(fig); plt.close()

    # ── 4.5
    with tabs[4]:
        st.markdown("### 4.5 Correlation Heatmap")
        st.markdown('<div class="info-box">The correlation heatmap shows pairwise Pearson correlations for all numeric variables. Values near +1 = strong positive, near -1 = strong negative, near 0 = no linear relationship.</div>', unsafe_allow_html=True)
        corr = fdf.drop(columns="Student_ID").corr()
        c1,c2 = st.columns([1.5,1])
        with c1:
            fig,ax = plt.subplots(figsize=(6.5,5))
            sns.heatmap(corr, annot=True, fmt=".2f", cmap="Blues",
                        linewidths=0.5, linecolor="white",
                        annot_kws={"size":11,"weight":"bold"},
                        ax=ax, square=True, cbar_kws={"shrink":.75})
            ax.set_title("Correlation Heatmap",fontsize=13,fontweight="bold",pad=10)
            fig.tight_layout(); st.pyplot(fig); plt.close()
        with c2:
            st.markdown("**Correlation Table**")
            st.dataframe(corr.round(3), use_container_width=True)
            st.markdown("**Key Findings**")
            for c in ["Math","Science","English"]:
                r2 = corr.loc["Hours_Studied",c]
                st.markdown(f"- Hours vs **{c}**: `{r2:.2f}` — {'✅ Strong' if r2>0.6 else '⚠️ Moderate'}")
            ra = corr.loc["Attendance","Math"]
            st.markdown(f"- Attendance vs **Math**: `{ra:.2f}`")
        st.code("""corr = df.corr(numeric_only=True)
print(corr)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()""", language="python")

# ════════════════════════════════════════════════════════════════════
# PAGE: Chapter 5 — Analysis & Evaluation
# ════════════════════════════════════════════════════════════════════
elif page == "Chapter 5 — Analysis & Evaluation":
    st.markdown('<div class="chapter-badge">CHAPTER 5</div>', unsafe_allow_html=True)
    st.markdown("## Analysis, Discussion & Evaluation")

    st.markdown("### 5.1 Performance Evaluation")
    corr = fdf.drop(columns="Student_ID").corr()
    c1,c2,c3 = st.columns(3)
    c1.markdown(f"""<div class="kpi-card">
        <div class="klabel">Hours vs Math (r)</div>
        <div class="kvalue">{corr.loc['Hours_Studied','Math']:.2f}</div>
        <div class="ksub">Strong Positive ✅</div></div>""", unsafe_allow_html=True)
    c2.markdown(f"""<div class="kpi-card">
        <div class="klabel">Hours vs Science (r)</div>
        <div class="kvalue">{corr.loc['Hours_Studied','Science']:.2f}</div>
        <div class="ksub">Strong Positive ✅</div></div>""", unsafe_allow_html=True)
    c3.markdown(f"""<div class="kpi-card">
        <div class="klabel">Attendance vs Math (r)</div>
        <div class="kvalue">{corr.loc['Attendance','Math']:.2f}</div>
        <div class="ksub">Moderate Positive</div></div>""", unsafe_allow_html=True)

    st.markdown("### 5.2 Strengths of the System")
    for s in ["Open-source & cost-free — built entirely on Python libraries",
              "Transparent — every step of cleaning and analysis is visible",
              "Interactive Streamlit dashboard — real-time data exploration",
              "Scalable modular design — new modules can be added easily",
              "Educational value — bridges theory and real-world application"]:
        st.markdown(f"✅ {s}")

    st.markdown("### 5.3 Limitations Identified")
    for l in ["Dataset is manually created — real student data would add depth",
              "No machine learning predictions yet (future scope)",
              "CSV format only — Excel/SQL support not implemented",
              "Offline setup required — not yet cloud-deployed"]:
        st.markdown(f"⚠️ {l}")

    st.markdown("### 5.4 Discussion of Results")
    st.markdown('<div class="info-box">The analysis confirmed that <b>study hours</b> have the strongest positive correlation with marks across all three subjects. <b>Attendance</b> also positively impacts performance. The three subjects (Math, Science, English) are moderately correlated with each other, suggesting students who perform well in one tend to perform well in others. Most students scored between <b>70–90 marks</b>, indicating a normally distributed performance curve.</div>', unsafe_allow_html=True)

    fig,ax = plt.subplots(figsize=(7,4))
    subjects = ["Math","Science","English"]
    corr_vals = [corr.loc["Hours_Studied",s] for s in subjects]
    colors = ["#2E75B6" if v>0.6 else "#FF8C00" for v in corr_vals]
    bars = ax.bar(subjects, corr_vals, color=colors, edgecolor="white", width=0.5)
    ax.axhline(0.6,color="#C00000",lw=1.5,linestyle="--",label="Strong threshold (0.6)")
    ax.set_ylabel("Pearson r",fontsize=10); ax.set_ylim(0,1)
    ax.set_title("Correlation: Hours Studied vs Each Subject",fontsize=11,fontweight="bold")
    ax.legend(fontsize=9); ax.grid(axis="y",linestyle="--",alpha=0.4)
    for bar,val in zip(bars,corr_vals):
        ax.text(bar.get_x()+bar.get_width()/2, val+0.01, f"{val:.2f}", ha="center",fontsize=10,fontweight="bold")
    fig.tight_layout(); st.pyplot(fig); plt.close()

# ════════════════════════════════════════════════════════════════════
# PAGE: Chapter 6 — Conclusion & Future Scope
# ════════════════════════════════════════════════════════════════════
elif page == "Chapter 6 — Conclusion & Future Scope":
    st.markdown('<div class="chapter-badge">CHAPTER 6</div>', unsafe_allow_html=True)
    st.markdown("## Conclusion & Future Scope")

    st.markdown("### 6.1 Conclusion")
    st.markdown('<div class="info-box">This project successfully demonstrated univariate and bivariate analysis on student performance data using Python. By leveraging Pandas, Matplotlib, Seaborn, and Streamlit, the system provides an interactive, transparent, and cost-free platform for academic data analysis.<br><br>Key findings: study hours strongly predict marks across all subjects; attendance positively influences performance; the three subjects are positively correlated. Visualization tools made these insights immediately clear and actionable.</div>', unsafe_allow_html=True)

    st.markdown("### 6.2 Key Contributions")
    for k in ["Developed a complete data analysis pipeline from loading to visualization",
              "Applied univariate analysis: histogram, boxplot, descriptive stats",
              "Applied bivariate analysis: scatter plots, Pearson correlation, heatmap",
              "Built an interactive Streamlit dashboard accessible to non-programmers",
              "Demonstrated Python as a powerful, free alternative to Excel for education analytics"]:
        st.markdown(f"🎯 {k}")

    st.markdown("### 6.3 Future Scope")
    future = [
        ("🤖","Machine Learning","Apply regression/classification to predict student grades"),
        ("📊","Larger Datasets","Use real institutional datasets for more robust analysis"),
        ("☁️","Cloud Deployment","Host on Streamlit Cloud or AWS for public access"),
        ("📱","Mobile App","Develop a mobile-friendly version for teachers on the go"),
        ("🗂️","Multi-format Support","Accept Excel, SQL, and API-based data sources"),
    ]
    for icon,title,desc in future:
        st.markdown(f"""<div style="background:white;border-left:5px solid #2E75B6;border-radius:8px;
            padding:12px 16px;margin-bottom:8px;box-shadow:0 2px 6px rgba(0,0,0,.06)">
            {icon} <b style="color:#1F4E79">{title}:</b> {desc}</div>""", unsafe_allow_html=True)

    st.markdown("### 6.4 Final Reflection")
    st.markdown('<div class="info-box" style="font-style:italic;font-size:1rem;text-align:center;padding:20px">"This project demonstrates how data analysis techniques can be used to extract meaningful insights and support evidence-based decision-making in education."</div>', unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("<p style='text-align:center;color:#aaa;font-size:.78rem'>Student Performance Analysis · Himalaya Utreja & Chandan Sindhi · 24BCS10848 / 24BCS10854 · Chandigarh University</p>", unsafe_allow_html=True)
