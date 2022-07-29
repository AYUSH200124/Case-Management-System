import Sidebar from "../../components/sidebar/Sidebar";
import Navbar from "../../components/navbar/Navbar";
import "./home.scss";
import Widget from "../../components/widget/Widget";
import Featured from "../../components/featured/Featured";
import Chart from "../../components/chart/Chart";
import Datatable from "../../components/datatable/Datatable"
import { useState, useEffect } from "react";
import axios from "axios";


function Home(){
const [details, caseDetails] = useState([])
useEffect(()=>{
    async function getAllDetails(){
        try {
            const details = await axios.get("http://127.0.0.1:8000/dashboard/")
            console.log(details.data)
            caseDetails(details.data)
        }catch (error){
            console.log(error)
        }
    }
    getAllDetails()
}, [ ] )

const Home = () => {
  return (
    <div className="home">
      <Sidebar />
      <div className="homeContainer">
        <Navbar />
        <div className="widgets">
          <Widget type="CRT" />
          <Widget type="CIP" />
          <Widget type="PC" />
          <Widget type="TC" />
        </div>
        <div className="listContainer">
          {/* <div className="listTitle">Recently registered Cases</div> */}

          {details && details.map( (item)=>(
               <Datatable
              username= {item.animal_type}
              img= {item.animal_picture_1}
              status={item.status}
              email={item.location}
              age={item.phone_number}

          />
          ))}
        </div>
      </div>
    </div>
  );
}};

export default Home;
