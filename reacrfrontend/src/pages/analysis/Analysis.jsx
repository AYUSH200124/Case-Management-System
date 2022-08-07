import Sidebar from "../../components/sidebar/Sidebar";
import Navbar from "../../components/navbar/Navbar";
import "./home.scss";
import Widget from "../../components/widget/Widget";
import Featured from "../../components/featured/Featured";
import Chart from "../../components/chart/Chart";
import Table from "../../components/table/Table";

const Analysis = () => {
  return (
    <div className="home">
      <Sidebar />
      <div className="homeContainer">
        <Navbar />
        <div className="widgets">
          <Widget type="1" />
          <Widget type="2" />
          <Widget type="3" />
          <Widget type="4" />
        </div>
        <div className="widgets">
          <Widget type="5" />
          <Widget type="6" />
          <Widget type="7" />
          <Widget type="8" />
        </div>
        <div className="charts">
          From : <input type="date" />
          To : <input type="date" />
          <br />
          <button className="btn-s">View Analysis</button>
          <label for="Status">Excel Export:</label>
          <select name="Status" id="Status">
            <option value="This_Year">This year</option>
            <option value="This_Month">This month</option>
            <option value="All_time" selected>All time</option>
          </select>
        </div>
        <div className="charts">
          {/* <Featured /> */}
          {/* <Chart title="Last 6 Months (Cases)" aspect={2 / 1} /> */}
        </div>
      </div>
    </div>
  );
};

export default Analysis;
