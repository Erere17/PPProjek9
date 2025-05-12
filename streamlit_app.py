import streamlit as st
import math

st.set_page_config(page_title=&quot;Metode 1 Isokinetik Pada Emisi Tidak Bergerak&quot;,
layout=&quot;centered&quot;)

# Title
st.title(&quot; Kalkulator Titik Sampling Pada Emisi Tidak Bergerak &quot;)
st.header(&quot;:blue[Metode 1 - Isokinetik Sampling]&quot;)

st.write(&quot;&quot;&quot;
Aplikasi ini akan menghitung lokasi titik sampling cerobong berdasarkan diameter dan
jarak terhadap gangguan aliran sesuai standar metode 1 isokinetik.
&quot;&quot;&quot;)

# Sidebar for input
with st.sidebar:
  st.header(&quot;Input Parameter&quot;)
  diameter = st.number_input("Diameter Cerobong (m)", min_value=0.1, step=0.01)
  panjang_nipple = st.number_input(&quot;Panjang Nipple (m)&quot;, min_value=0.0, step=0.1)
  upstream = st.number_input(&quot;Jarak Upstream dari Gangguan (m)&quot;, min_value=0.0, step=0.1)
  downstream = st.number_input(&quot;Jarak Downstream dari Gangguan (m)&quot;, min_value=0.0, step=0.1)

# Divider
st.markdown(&quot;---&quot;)

# Fungsi menentukan jumlah titik lintas
def tentukan_jumlah_titik(diameter, upstream, downstream):
  if diameter &gt;= 0.61:
    if upstream &gt;= 8 * diameter and downstream &gt;= 2 * diameter:
    return 12
  elif upstream &gt;= 4 * diameter and downstream &gt;= 1 * diameter:
  return 10
else:
return 8
elif: 0.3 &lt;= diameter &lt; 0.61:
return 8
else:
return 6

# Tombol Hitung
if st.button(&quot;Hitung Titik Sampling&quot;):
if diameter &gt; 0:
jumlah_titik = tentukan_jumlah_titik(diameter, upstream, downstream)
radius = diameter / 2
st.subheader(&quot; Hasil Perhitungan&quot;)
st.write(f&quot;Diameter cerobong: **{diameter} m**&quot;)
st.write(f&quot;Jumlah titik lintas (otomatis): **{jumlah_titik} titik**&quot;)

hasil = []
for i in range(1, jumlah_titik + 1):
  posisi = radius * math.sqrt((i - 0.5) / jumlah_titik)
  jarak_dari_tepi = round(radius - posisi, 3)
  hasil.append(jarak_dari_tepi)
  st.write(f&quot;Titik {i}: {jarak_dari_tepi} m dari tepi cerobong&quot;)
  st.subheader(&quot; Tabel Titik Sampling&quot;)
  st.table({f&quot;Titik {i+1}&quot;: [f&quot;{hasil[i]} m&quot;] for i in range(len(hasil))})

st.success(&quot;Perhitungan titik sampling selesai.&quot;)
else:
st.error(&quot;Masukkan diameter cerobong yang valid.&quot;)

st.markdown(&quot;---&quot;)
st.caption(&quot; Dibuat dengan Streamlit berdasarkan metode sampling isokinetik sesua
standar EPA.&quot;)
