import streamlit as st
import pandas as pd
import os
from datetime import datetime
# Streamlit UI
st.title("🏗️GULF CONCRETE & BLOCKS🚧")
st.subheader(">>>>>American University of Ras Al-khaimah<<<<<<   ")
st.subheader("🚒Mobile Units Preventive Maintenance Schedule👷🏼‍♂️")
st.write("By: Sara Tesfaye &  Henok Mundino")

with st.expander("🦺 Concrete Pump Safety Notes", expanded=False):

    st.markdown("#### 🚧 General Awareness")
    st.markdown("""
    - Concrete pumping involves both heavy machinery and highly technical operations.
    - Safe operation demands more than just wearing PPE—understanding the equipment is essential.
    - Awareness of hazards is key to applying the right safety precautions.
    """)

    st.markdown("#### ✅ Before Pumping")
    st.markdown("""
    🟢Site & Setup Safety
    - Conduct a pre-operation **site inspection**: check terrain, slope, and obstructions.
    - Verify that **ground is stable and level** for outriggers; use pads or cribbing if needed.
    - Ensure proper **lighting conditions** are available, especially for early/late work.
    - Check that all crew members are equipped with full **PPE** (helmet, vest, gloves, boots, goggles).
    - Inspect **hoses, clamps, and lines** for cracks, wear, or corrosion.
    - Confirm the **hopper grate is secure** and never removed during operation.
    - Test **emergency stop buttons** and **reverse mode functionality**.
    - Verify the **agitator and remote control** are working properly before starting.
    """)

    st.markdown("#### 🟡 During Pumping")
    st.markdown("""
    - Maintain **constant visual or radio contact** between pump operator and crew.
    - Never place hands or tools into the **hopper while the pump is running**.
    - Regularly monitor **system pressure** and shut down if pressure spikes unexpectedly.
    - Ensure **only trained personnel** are near the pump during operation.
    - Resume pumping only after clearly **communicating with all crew**.
    - Watch for signs of **blockage** (e.g., loss of flow, erratic cycling) and stop operation before troubleshooting.
    - Never allow unauthorized or untrained individuals near the boom or line during a pour.
    """)

    st.markdown("#### 🔴 After Pumping")
    st.markdown("""
    ✅ Shutdown & Cleanup Safety
    - **Relieve pressure** before disconnecting or cleaning any part of the pump or line.
    - Clean lines using **low-pressure water** or **approved sponge/slurry balls**—avoid high-pressure air unless designed for it.
    - Fully **fold and lock** all boom sections and outriggers before moving the truck.
    - **Power off and disconnect remotes** to prevent accidental activation.
    - Log any **maintenance issues or hazards** noted during operation.
    - Recheck all components before storage or relocation to avoid next-job risks.
    """)


    st.markdown("#### ⚠️ Hose Hazards")
    st.markdown("""
    One of the most common hazards comes from releasing compressed air in hoses, which can whip violently and cause injury.
    
    - Stand back when releasing compressed air to avoid hose whipping.
    - Avoid double-end or double-S hose attachments; they're heavier and more dangerous.
    - Monitor air pressure at the discharge point to avoid pressure pockets.
    """)

    st.markdown("#### ⚡ Power Line Contact")
    st.markdown("""
    Contact with power lines is often fatal and usually due to operator error.

    - Train workers on power-line safety and inspection routines.
    - Keep at least 20 feet of clearance from all power lines.
    - Verify and document power-line locations and stamps on every job site.
    """)

    st.markdown("#### 🧴 Concrete Burns")
    st.markdown("""
    Skin contact with wet cement can cause severe alkaline burns and even blood poisoning.

    - Wear full PPE from head to toe to protect skin.
    - Rinse affected skin with pH-neutral or slightly acidic solution like vinegar.
    - Always wash concrete-contaminated clothing before reuse.
    """)

    st.markdown("#### 🔌 Electrical Issues with the Truck")
    st.markdown("""
    Electrical faults from poor maintenance can shock operators or disable equipment.

    - Check alternator output; it should be at least 13.6 VDC.
    - Inspect and clean battery and ground connections.
    - Load test the battery to ensure proper amperage.
    """)

    st.markdown("#### 💧 Hydraulic Leaks")
    st.markdown("""
    Leaks can disable equipment, harm the environment, and pose slipping or contact hazards.

    - Shut off the equipment immediately if a leak is detected.
    - Contain and clean hydraulic fluid to prevent spread.
    """)

    st.markdown("#### 🏗️ Boom Awareness and Placement")
    st.markdown("""
    Improper boom handling can damage equipment or infrastructure and cause injury.

    - Always be aware of the boom’s position and surroundings.
    - Inspect for damage if the boom contacts another object.
    - Always fold and lock boom and outriggers before moving.
    - Never use a boom as a hoisting device.
    """)

    st.markdown("#### 🧪 Rough Mixes")
    st.markdown("""
    Poorly batched concrete can block hoses and compromise structural quality.

    - Confirm the correct rock quantity to maintain proper flow.
    - Ensure rocks are sized appropriately to avoid packing.
    - Use multiple aggregate sizes for a well-flowing mix.
    """)

    st.markdown("#### 🌡️ Oil Leaks")
    st.markdown("""
    High-temperature oil leaks can cause burns or injection injuries.

    - Never attempt to stop a pressurized oil leak by hand or rag—even with gloves.
    - Shut down and cool the machine before addressing oil leaks.
    """)

    st.markdown("#### 🔧 Holding Valve Dangers")
    st.markdown("""
    Removing a pressurized holding valve can cause severe injury.

    - Always verify zero pressure before removing a valve.
    - Do not remove valves without proper boom support and rest time.
    - Unlatch holding valves slowly and cautiously.
    """)

    st.markdown("#### 💨 Compressed Air")
    st.markdown("""
    Using compressed air to clear booms can result in dangerous explosions of concrete.

    - Never use compressed air to clear a full boom.
    - Always check and relieve pressure before removing clamps.
    - Use a shovel or tool to maintain safe distance while unclamping.
    """)

    st.markdown("#### ✅ Final Reminder")
    st.markdown("""
    - Prioritize safety through centralized systems and daily discipline.
    """)


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
