# Importing necessary libraries
import streamlit as st
import numpy as np

# Title of the web app
st.title('Air Quality in Huairou')

# GitHub CSV file URL
csv_url = 'https://raw.githubusercontent.com/chindyfebryan/air-quality-dashboard/main/all_data.csv'

# Function to load CSV data
def load_data(url):
    response = requests.get(url)
    content = response.content
    csv_file = pd.read_csv(pd.compat.StringIO(content.decode('utf-8')))
    return csv_file

# Load CSV data
huairou_df = load_data(csv_url)

monthly_so2 = huairou_df.groupby('month')['SO2'].mean()
monthly_no2 = huairou_df.groupby('month')['NO2'].mean()

huairou_df['hour'] = pd.to_datetime(huairou_df['hour'], format='%H').dt.hour

aggregated_data = huairou_df.groupby('hour').agg({
    'PM2.5': ['mean'],
    'PM10': ['mean'],
    'SO2': ['mean'],
    'NO2': ['mean'],
    'O3': ['mean']
}) 

st.write(monthly_so2)

st.subheader("Kesimpulan Pertanyaan 1:")
st.write("Terlihat bahwa konsentrasi SO2 cenderung lebih tinggi pada awal tahun, terutama pada bulan Januari, Februari, dan Maret. Hal ini mungkin terkait dengan kondisi cuaca dan pola emisi dari berbagai sumber pada periode tersebut. Konsentrasi SO2 kemudian menurun secara bertahap sepanjang tahun, mencapai titik terendah pada bulan Agustus, sebelum kembali meningkat menuju akhir tahun. Sedangkan konsentrasi NO2 juga menunjukkan pola yang mirip dengan konsentrasi SO2. Konsentrasi NO2 mencapai puncak tertinggi pada bulan November dan Desember.")

st.subheader("Kesimpulan Pertanyaan 2:")
st.write("PM2.5 dan PM10: Terlihat bahwa konsentrasi PM2.5 dan PM10 cenderung tinggi pada malam hari dan pagi hari, yang mungkin terkait dengan aktivitas transportasi dan industri yang lebih rendah selama periode tersebut.\n\nSO2: Konsentrasi SO2 terlihat meningkat di pagi hari dan kemudian menurun sepanjang siang dan sore hari. Hal ini mungkin terkait dengan polusi udara dari industri dan transportasi yang aktif pada pagi hari.\n\nNO2: Konsentrasi NO2 cenderung tinggi di pagi hari, kemudian menurun menjelang sore hari. Ini juga bisa terkait dengan polusi dari kendaraan bermotor yang beroperasi pada waktu tersebut.\n\nO3: Konsentrasi O3, yang merupakan indikator kualitas udara yang lebih baik, cenderung meningkat di siang hari karena paparan sinar matahari dan reaksi kimia di atmosfer. Namun, terdapat perubahan yang cukup signifikan di malam hari.")
