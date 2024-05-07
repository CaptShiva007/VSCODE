document.addEventListener('DOMContentLoaded', () => {
    const socket = io();

    // Initialize Chart.js
    const ctx = document.getElementById('trafficChart').getContext('2d');
    const trafficChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'Network Traffic',
                data: [],
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                x: {
                    type: 'linear',
                    position: 'bottom'
                },
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Handle initial data event
    socket.on('initial_data', data => {
        trafficChart.data.labels = data.x_data;
        trafficChart.data.datasets[0].data = data.y_data;
        trafficChart.update();
    });

    // Handle update_graph event
    socket.on('update_graph', data => {
        // Push new data point to the chart
        trafficChart.data.labels.push(trafficChart.data.labels.length + 1);
        trafficChart.data.datasets[0].data.push(data.y_data);
        // Remove oldest data point if exceeding window size
        if (trafficChart.data.labels.length > 30) {
            trafficChart.data.labels.shift();
            trafficChart.data.datasets[0].data.shift();
        }
        trafficChart.update(); // Update the chart
    });

    // Start packet sniffing when the page loads
    socket.emit('start_sniffing', 'your_interface_name');
});
