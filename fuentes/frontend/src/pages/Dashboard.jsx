import Card from "../components/Card";
import PendingService from "../components/PendingService";
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS } from 'chart.js/auto';

export default function Dashboard() {
    return <div className="w-full h-full">
        <div className="flex-col md:flex-row md:flex justify-evenly items-center">
            <Card title={"Pendientes"} className="flex-grow">
              <PendingService
                timeRemaining="3:00"
                titleService="Examen"
                descriptionService="Practica calificada Algoritmica 1"
                workerInCharge="Asthri Joanne Pardave Jara"
                topics={['C++', 'Arrays', 'Bucles for']}
              />    
            </Card>
            <Card title={"Ganancias totales"} className="flex-grow">
                <Bar
                data={{
                    labels: ["January", "February", "March", "April", "May", "June"],
                    datasets: [{
                      label: 'My First Dataset',
                      data: [65, 59, 80, 81, 56, 55],
                      backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(255, 159, 64, 0.2)',
                        'rgba(255, 205, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                      ],
                      borderColor: [
                        'rgb(255, 99, 132)',
                        'rgb(255, 159, 64)',
                        'rgb(255, 205, 86)',
                        'rgb(75, 192, 192)',
                        'rgb(54, 162, 235)',
                        'rgb(153, 102, 255)',
                      ],
                      borderWidth: 1
                    }]
                  }}
                options = {{
                  scales: {
                    y: {
                      beginAtZero: true
                    }
                  }
                }}
                />
            </Card>
        </div>
    </div>
}