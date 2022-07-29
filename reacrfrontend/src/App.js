import Home from "./pages/home/Home";
import Analysis from "./pages/analysis/Analysis";
import Login from "./pages/login/Login";
import List from "./pages/list/List";
import Single from "./pages/single/Single";
import New from "./pages/new/New";
import New1 from "./pages/new1/New1";
import New2 from "./pages/new2/New2";
import New3 from "./pages/new3/New3";
import New4 from "./pages/new4/New4";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { productInputs, userInputs, userInputs1, userInputs2, userInputs3, userInputs4} from "./formSource";
import "./style/dark.scss";
import { useContext } from "react";
import { DarkModeContext } from "./context/darkModeContext";



function App() {
  const { darkMode } = useContext(DarkModeContext);






  return (
    <div className={darkMode ? "app dark" : "app"}>
      <BrowserRouter>
        <Routes>
          <Route path="/">
            <Route index element={<Home />} />
            <Route path="analysis" element={<Analysis />} />
            <Route path="login" element={<Login />} />
            <Route path="users">
                <Route index element={<List />} />
                <Route path=":userId" element={<Single />} />
                <Route path="new">
                <Route index element={<New inputs={userInputs} title="Reporter's Details"/>} />
                    <Route path="new1">
                    <Route index element={<New1 inputs={userInputs1} title="Further Animal Details"/>} />
                      <Route path="new2">
                      <Route index element={<New2 inputs={userInputs2} title="Medical Details"/>} />
                        <Route path="new3">
                        <Route index element={<New3 inputs={userInputs3} title="Operation Details"/>} />
                          <Route path="new4">
                          <Route index element={<New4 inputs={userInputs4} title="Post Operation Details"/>} />
                          </Route>
                        </Route>
                      </Route>
                    </Route>
                </Route>
            </Route>
            <Route path="products">
              <Route index element={<List />} />
              <Route path=":productId" element={<Single />} />
              <Route
                path="new"
                element={<New inputs={productInputs} title="Add New Product" />}
              />
            </Route>
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
