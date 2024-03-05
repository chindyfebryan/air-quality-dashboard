# Importing necessary libraries
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import requests

# Title of the web app
st.title('Air Quality in Huairou')

csv_url = 'https://raw.githubusercontent.com/chindyfebryan/air-quality-dashboard/main/all_data.csv'

# Importing data
huairou_df = pd.read_csv(csv_url)

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

# Visualizations
st.subheader('Bagaimana pola bulanan konsentrasi SO2 dan NO2 di Huairou?')
plt.figure(figsize=(10, 6))
plt.bar(monthly_so2.index - 0.2, monthly_so2.values, width=0.4, color='blue', label='SO2')
plt.bar(monthly_no2.index + 0.2, monthly_no2.values, width=0.4, color='green', label='NO2')
plt.title('Perbandingan Pola Bulanan Konsentrasi SO2 dan NO2 di Huairou')
plt.xlabel('Bulan')
plt.ylabel('Konsentrasi Rata-rata')
plt.xticks(range(1, 13))  # Label bulan dari 1 hingga 12
plt.legend()
plt.grid(True)
st.pyplot()

st.subheader('Bagaimana kualitas udara berdasarkan jam dalam satu hari di Huairou?')
aggregated_data.plot(kind='line', figsize=(12, 8), marker='o')
plt.title('Perbandingan Kualitas Udara Berdasarkan Jam')
plt.xlabel('Jam dalam Sehari')
plt.ylabel('Rata-rata Kualitas Udara')
plt.xticks(range(24))
plt.grid(True)
plt.legend(title='Parameter')
st.pyplot()

st.subheader("Kesimpulan Pertanyaan 1:")
st.write("Terlihat bahwa konsentrasi SO2 cenderung lebih tinggi pada awal tahun, terutama pada bulan Januari, Februari, dan Maret. Hal ini mungkin terkait dengan kondisi cuaca dan pola emisi dari berbagai sumber pada periode tersebut. Konsentrasi SO2 kemudian menurun secara bertahap sepanjang tahun, mencapai titik terendah pada bulan Agustus, sebelum kembali meningkat menuju akhir tahun. Sedangkan konsentrasi NO2 juga menunjukkan pola yang mirip dengan konsentrasi SO2. Konsentrasi NO2 mencapai puncak tertinggi pada bulan November dan Desember.")

st.subheader("Kesimpulan Pertanyaan 2:")
st.write("PM2.5 dan PM10: Terlihat bahwa konsentrasi PM2.5 dan PM10 cenderung tinggi pada malam hari dan pagi hari, yang mungkin terkait dengan aktivitas transportasi dan industri yang lebih rendah selama periode tersebut.\n\nSO2: Konsentrasi SO2 terlihat meningkat di pagi hari dan kemudian menurun sepanjang siang dan sore hari. Hal ini mungkin terkait dengan polusi udara dari industri dan transportasi yang aktif pada pagi hari.\n\nNO2: Konsentrasi NO2 cenderung tinggi di pagi hari, kemudian menurun menjelang sore hari. Ini juga bisa terkait dengan polusi dari kendaraan bermotor yang beroperasi pada waktu tersebut.\n\nO3: Konsentrasi O3, yang merupakan indikator kualitas udara yang lebih baik, cenderung meningkat di siang hari karena paparan sinar matahari dan reaksi kimia di atmosfer. Namun, terdapat perubahan yang cukup signifikan di malam hari.")

st.set_option('deprecation.showPyplotGlobalUse', False)
