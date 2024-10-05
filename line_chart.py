from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource
import pandas as pd
from datetime import datetime, timedelta

# Menyiapkan data
data = {
    'timestamp': [datetime(2024, 7, 30, 10, 23, 42) + timedelta(seconds=i) for i in range(10)],
    'transfer': [197, 0, 94.5, 86.6, 214, 0, 126, 189, 0, 252],
    'bitrate': [1.61, 0.00, 774, 710, 1.75, 0.00, 1.03, 1.55, 0.00, 2.06]
}

# Mengubah data menjadi DataFrame
df = pd.DataFrame(data)

# Membuat ColumnDataSource untuk Bokeh
source = ColumnDataSource(df)

# Menyiapkan output file HTML
output_file("bandwidth_test_output.html")

# Membuat figure
p = figure(title="Iperf Transfer and Bitrate Over Time", x_axis_label='Timestamp', x_axis_type='datetime', y_axis_label='Value', width=800, height=400)

# Menambahkan line untuk transfer
p.line('timestamp', 'transfer', source=source, legend_label='Transfer (KBytes)', line_color='blue', line_width=2)

# Menambahkan scatter untuk transfer
p.scatter('timestamp', 'transfer', source=source, fill_color='blue', size=8)

# Menambahkan line untuk bitrate
p.line('timestamp', 'bitrate', source=source, legend_label='Bitrate (Kbits/sec)', line_color='orange', line_width=2)

# Menambahkan scatter untuk bitrate
p.scatter('timestamp', 'bitrate', source=source, fill_color='orange', size=8)

# Menambahkan grid dan legenda
p.grid.grid_line_alpha = 0.3
p.legend.location = "top_left"
p.legend.click_policy = "hide"

# Menampilkan chart dan menyimpannya ke file HTML
show(p)
