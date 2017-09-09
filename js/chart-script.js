
$.getJSON("db.json", function(json) {
    console.log(json);
    var user;
    var current_user_id = "150";
    var trips = json.user[0].trips;
    
    var amountOfRides = trips.length;
    
    var tripnum = 0
    var totalMileage = 0;
    var totalMoneySpent = 0;
    var cumulativeMileage = []
    var cumulativeMartaMoney = []
    var cumulativeCarMoney = []
    var dates = ["05", "06", "07", "08", "09", "12", "13", "14", "15", "16",]
    for (i = 0; i < 10; i++) {
        console.log(trips[0]);
        tripnum = tripnum + 1
        totalMileage = totalMileage + trips[0].trip_mileage;
        totalMoneySpent = totalMoneySpent + 2.5;
        cumulativeMileage = cumulativeMileage.concat([totalMileage]);
        cumulativeMartaMoney = cumulativeMartaMoney.concat([totalMoneySpent]);
        cumulativeCarMoney = cumulativeCarMoney.concat([(totalMileage/30)*30]);
    }
    console.log(tripnum);
    console.log(totalMileage);
    console.log(totalMoneySpent);
    console.log(cumulativeMileage);
    console.log(cumulativeMartaMoney);
    console.log(cumulativeCarMoney);
    
    var ctx = document.getElementById("canvas");
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: dates,
            datasets: [{
                label: '$ Spent on Marta',
                data: cumulativeMartaMoney,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            },{
                label: 'Potential $ Spent on Gasoline',
                data: cumulativeCarMoney,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }

                      ]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });
    
    
});


    