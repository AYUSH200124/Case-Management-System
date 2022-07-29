import "../new/new.scss";
import Sidebar from "../../components/sidebar/Sidebar";
import Navbar from "../../components/navbar/Navbar";
import DriveFolderUploadOutlinedIcon from "@mui/icons-material/DriveFolderUploadOutlined";
import { useState } from "react";
import { Link } from "react-router-dom";
const New2 = ({ inputs, title }) => {
  const [file, setFile] = useState("");

  return (
    <div className="new">
      <Sidebar />
      <div className="newContainer">
        <Navbar />
        <div className="top">
          <h1>{title}</h1>
        </div>
        <div className="bottom">
          <div className="left">
            <img
              src={
                file
                  ? URL.createObjectURL(file)
                  : "https://icon-library.com/images/no-image-icon/no-image-icon-0.jpg"
              }
              alt=""
            />
          </div>
          <div className="right">
            <form>
              <div className="formInput">
                <label htmlFor="file">
                  Blood Report:{" "}
                  <DriveFolderUploadOutlinedIcon className="icon" />
                </label>
                <input
                  type="file"
                  id="file"
                  onChange={(e) => setFile(e.target.files[0])}
                  style={{ display: "none" }}
                />
              </div>
              <label for="Status">Status:</label>
              <select name="Status" id="Status">
                <option value="Reported">Reported</option>
                <option value="Admitted">admitted</option>
                <option value="Blood test done" selected>
                  Blood test done
                </option>
                <option value="Operation started">Operation started</option>
                <option value="Post Operation">Post Operation</option>
                <option value="Released">Released</option>
              </select>
              {inputs.map((input) => (
                <div className="formInput" key={input.id}>
                  <label>{input.label}</label>
                  <input type={input.type} placeholder={input.placeholder} />
                </div>
              ))}

              <Link to="/users/new/new1" className="link">
                <button className="btn-s">Move back to Animal Details</button>
              </Link>
              <button className="btn-s">Save Here</button>
              <Link to="/users/new/new1/new2/new3" className="link">
                <button className="btn-s">Move to Operation Details</button>
              </Link>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default New2;
