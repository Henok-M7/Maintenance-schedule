import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Mapping of unit types to their available brands and unit IDs
unit_data = {
    "Concrete Pump": {
        "putzmeister": ["PU10", "PU11", "PU19", "PU20", "PU23", "PU24", "PU25", "PU26", "PU27", "PU29", "PU30"],
        "schwing": ["PU28"]
    },
    "Mixer": {
        "mercedes": ["TM089", "TM090","TM091","TM092","TM093","TM104","TM105","TM106","TM107","TM108","TM109","TM110","TM111","TM112","TM113"],
        "renault": ["TM072","TM73","TM074","TM075","TM076","TM077"],
        "scania": ["TM078","TM079","TM080","TM081","TM082","TM083","TM084","TM085","TM086","TM087","TM088","TM094","TM095","TM096","TM097","TM098","TM099","TM100","TM101","TM102","TM103"]
    },
    "Wheel Loader": {
        "caterpiler": ["SH07","SH08","SH09","SH10","SH11","SH12"]
    },
    "Truck Head": {
        "hino": ["TR037","TR038","TR044","TR045","TR048","TR049","TR050",]
    },
    "Stationary Pump": {
        "putzmeister": ["SP03","SP05"]
    },
    "Placing Boom": {
        "boom_makina": ["PB01","PB02"],
        "trumax":["PB03","PB04"]
    },
    "Cement Tanker": {
        "cement_tanker": ["CT008","CT010","CT011","CT012","CT013","CT014"],
    },
    "trailer box": {
        "trailer_box": ["TP001","TP015","TP019","TP020","TP021","TP022","TP025","TP026","TP027"]
    },
    "Spider Boom": {
        "truemax": ["SB"]
    },
    "Dust Cleaning Machine": {
        "armadillo": ["armadillo"]
    }
}

# Streamlit UI
st.title("🏗️GULF CONCRETE & BLOCKS🚧 \n 🚒Mobile Units Preventive Maintenance Schedule👷🏼‍♂️")

# Step 1: Select Unit Type
unit_type = st.selectbox("Select Mobile Unit Type:", list(unit_data.keys()))

if unit_type:
    brand_map = unit_data[unit_type]
    selected_brand = st.selectbox("Select Brand:", list(brand_map.keys()))

    if selected_brand:
        selected_id = st.selectbox("Select Unit ID:", brand_map[selected_brand])

        # Construct file path
        excel_path = f"schedule/{unit_type.lower().replace(' ', '_')}/{selected_brand.lower()}.xlsx"

        if os.path.exists(excel_path):
            try:
                # Step 2: Read available sheet names as maintenance frequencies
                xls = pd.ExcelFile(excel_path)
                frequencies = xls.sheet_names
                frequency = st.selectbox("Select Maintenance Frequency:", frequencies)

                df = pd.read_excel(excel_path, sheet_name=frequency)
                df["Completed"] = False

                st.write(f"### {frequency.capitalize()} Maintenance Tasks")
                completed_tasks = []

                for i, task in enumerate(df["Task"]):
                    completed = st.checkbox(task, key=f"task_{i}")
                    if completed:
                        completed_tasks.append(task)

                if st.button("Done"):
                    log_path = excel_path  # reuse the same workbook
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    log_entry = pd.DataFrame({
                        "Timestamp": [timestamp] * len(completed_tasks),
                        "Unit Type": [unit_type] * len(completed_tasks),
                        "Brand": [selected_brand] * len(completed_tasks),
                        "Unit ID": [selected_id] * len(completed_tasks),
                        "Frequency": [frequency] * len(completed_tasks),
                        "Task": completed_tasks
                    })

                    # Append or create log sheet
                    try:
                        with pd.ExcelWriter(log_path, engine="openpyxl", mode="a", if_sheet_exists="overlay") as writer:
                            existing_log = pd.read_excel(log_path, sheet_name="maintenance_log")
                            full_log = pd.concat([existing_log, log_entry], ignore_index=True)
                            full_log.to_excel(writer, sheet_name="maintenance_log", index=False)
                    except:
                        with pd.ExcelWriter(log_path, engine="openpyxl", mode="a") as writer:
                            log_entry.to_excel(writer, sheet_name="maintenance_log", index=False)

                    st.success("Maintenance log has been recorded!")

            except Exception as e:
                st.error(f"Could not read sheet '{frequency}' in {selected_brand}.xlsx: {e}")
        else:
            st.error(f"File not found: {excel_path}")
