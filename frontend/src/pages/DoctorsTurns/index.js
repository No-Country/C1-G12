import { useState } from "react"
import { users } from "../../dummybd"
import "./styles.css"
import { Link } from "react-router-dom"
import { Helmet } from "react-helmet"

//Componente donde se veran los doctores disponibles y podrás seleccionar con quien tomar un turno si estas logueado
export default function DoctorsTurns() {
  const [doctors, setDoctors] = useState(
    users.filter((user) => user.type === "doctor" && user.active)
  )

  return (
    <>
      <Helmet>
        <title>Clinic | Meet Our Doctors</title>
        <meta name="description" content="Meet our doctors and take a turn " />
      </Helmet>
      <section className="OurDoctors">
        <h2>doctors</h2>
        <section className="list-turns">
          {doctors.map((doctor) => (
            <figure key={doctor.id}>
              <h2>
                {doctor.name} {doctor.surname}
              </h2>
              <span>{doctor.specialty}</span>
              <Link to="/Turn" className="button">
                Take turn
              </Link>
            </figure>
          ))}
        </section>
      </section>
    </>
  )
}
