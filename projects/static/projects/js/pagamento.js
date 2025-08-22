 // Payment Analytics Chart
        const ctx = document.getElementById('paymentChart').getContext('2d');
        const paymentChart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['Pagamentos Concluídos', 'Pagamentos Pendentes', 'Pagamentos Falhados', 'Reembolsos'],
                datasets: [{
                    data: [65, 20, 8, 7],
                    backgroundColor: [
                        '#10B981',
                        '#F59E0B', 
                        '#EF4444',
                        '#6B7280'
                    ],
                    borderWidth: 2,
                    borderColor: '#ffffff'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: {
                            padding: 20,
                            usePointStyle: true,
                            font: {
                                size: 12
                            }
                        }
                    }
                },
                cutout: '70%'
            }
        });