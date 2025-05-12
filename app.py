import streamlit as st
import math

st.set_page_config(page_title=&quot;Metode 1 Isokinetik Pada Emisi Tidak Bergerak&quot;,
layout=&quot;centered&quot;)

# Title
st.title(&quot;�� Kalkulator Titik Sampling Pada Emisi Tidak Bergerak ��&quot;)
st.header(&quot;:blue[Metode 1 - Isokinetik Sampling]&quot;)

# Description
st.write(&quot;&quot;&quot;
Aplikasi ini membantu menghitung titik sampling pada cerobong untuk metode isokinetik
berdasarkan jumlah titik lintas dan diameter cerobong.
&quot;&quot;&quot;)

# Sidebar for input
with st.sidebar:
st.header(&quot;Input Parameter&quot;)
diameter = st.number_input(&quot;Diameter Cerobong (m)&quot;, min_value=1.0, step=0.1)
jumlah_titik = st.number_input(&quot;Jumlah Titik Lintas&quot;, min_value=1, step=1)
panjang_nipple = st.number_input(&quot;Panjang Nipple (m)&quot;, min_value=0.0, step=0.1)
upstream = st.number_input(&quot;Jarak Upstream (m)&quot;, min_value=0.0, step=0.1)
downstream = st.number_input(&quot;Jarak Downstream (m)&quot;, min_value=0.0, step=0.1)

# Divider
st.markdown(&quot;---&quot;)

# Tombol untuk menghitung
if st.button(&quot;Hitung Titik Sampling&quot;):
if diameter and jumlah_titik:
radius = diameter / 2
st.subheader(&quot;�� Titik Sampling yang Direkomendasikan&quot;)
st.write(f&quot;Diameter cerobong: **{diameter} m**&quot;)
st.write(f&quot;Jumlah titik lintas: **{jumlah_titik} titik**&quot;)

hasil = []
for i in range(1, int(jumlah_titik) + 1):
posisi = radius * math.sqrt((i - 0.5) / jumlah_titik)
jarak_dari_tepi = round(radius - posisi, 2)
hasil.append(jarak_dari_tepi)
st.write(f&quot;Titik {i}: {jarak_dari_tepi} m dari tepi cerobong&quot;)

st.success(&quot;Perhitungan selesai.&quot;)

# Optional: Tampilkan tabel
st.subheader(&quot;�� Tabel Titik Sampling&quot;)
st.table({f&quot;Titik {i+1}&quot;: [f&quot;{hasil[i]} m&quot;] for i in range(len(hasil))})
else:
st.error(&quot;Masukkan diameter dan jumlah titik yang valid.&quot;)

st.markdown(&quot;---&quot;)
st.caption(&quot;�� Dibuat dengan Streamlit untuk simulasi edukatif metode samplin
isokinetik.&quot;)
