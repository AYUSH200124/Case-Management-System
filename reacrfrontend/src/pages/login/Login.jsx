import "./login.scss";
import pic from "./strayscue-logo.jpg";

export default function App() {
  return (
    <div className="App">
      <h4> </h4>
      <div className="login-page">
        <div className="form">
          <div className="login">
            <div className="login-header">
              <img className="logo" src={pic} alt="img" />

              <br />

              <h1>Strayscue Dashboard</h1>
              <h5>Enter Your Username and Password</h5>
            </div>
          </div>
          <form className="login-form" method="POST" action="{% url 'login' %}">
            <input type="text" name="username" placeholder="username" />
            <input type="password" name="password" placeholder="password" />
            <button>login</button>
          </form>
        </div>
      </div>
    </div>
  );
}
