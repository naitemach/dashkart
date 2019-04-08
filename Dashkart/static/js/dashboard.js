/* globals Chart:false, feather:false */

(function () {
  'use strict'

  feather.replace()

  // Graphs
  var hrx = document.getElementById('hrChart')
  // eslint-disable-next-line no-unused-vars
  var hrChart = new Chart(hrx, {
    type: 'line',
    data: {
      labels: [
        '11:00',
        '12:00',
        '13:00',
        '14:00',
        '15:00',
        '16:00',
        '17:00'
      ],
      datasets: [{
        data: [
          89,
          90,
          84,
          80,
          85,
          88,
          83
        ],
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',
        borderWidth: 4,
        pointBackgroundColor: '#007bff'
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: false
      }
    }
  })

 var bpx = document.getElementById('bpChart')
  // eslint-disable-next-line no-unused-vars
  var bpChart = new Chart(bpx, {
    type: 'line',
    data: {
      labels: [
        '11:00',
        '12:00',
        '13:00',
        '14:00',
        '15:00',
        '16:00',
        '17:00'
      ],
      datasets: [{
        data: [
          99,
          105,
          110,
          112,
          108,
          102,
          110
        ],
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',
        borderWidth: 4,
        pointBackgroundColor: '#007bff'
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: false
      }
    }
  })

 var rpx = document.getElementById('rpChart')
  // eslint-disable-next-line no-unused-vars
  var rpChart = new Chart(rpx, {
    type: 'line',
    data: {
      labels: [
        '11:00',
        '12:00',
        '13:00',
        '14:00',
        '15:00',
        '16:00',
        '17:00'
      ],
      datasets: [{
        data: [
          16,
          15,
          13,
          16,
          14,
          17,
          14
        ],
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',
        borderWidth: 4,
        pointBackgroundColor: '#007bff'
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: false
      }
    }
  })
 

var tpx = document.getElementById('tpChart')
  // eslint-disable-next-line no-unused-vars
  var tpChart = new Chart(tpx, {
    type: 'line',
    data: {
      labels: [
        '11:00',
        '12:00',
        '13:00',
        '14:00',
        '15:00',
        '16:00',
        '17:00'
      ],
      datasets: [{
        data: [
          98.6,
          98.8,
          98.5,
          98.4,
          98.0,
          97.9,
          98.0
        ],
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',
        borderWidth: 4,
        pointBackgroundColor: '#007bff'
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: false
      }
    }
  })

}())