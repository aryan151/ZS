import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import SideBar from "./components/SideBar/SideBar";
import LoadingScreen from "./components/LoadingScreen";
import Splash from "./components/Splash/Splash";
import { authenticate } from "./store/session";
import RootPage from "./components/RootPage";
import { setTheme } from "./store/theme";

function App() {
	const [loaded, setLoaded] = useState(false);
	const [showSidebar, setShowSidebar] = useState();
	const [showDark, setShowDark] = useState();
	const theme = useSelector(state => state.theme); 
	const toggleSidebar = () => {
		setShowSidebar(!showSidebar);
		localStorage.setItem('sidebar', !showSidebar)
	}
	const toggleDark = () => {
		setShowDark(!showDark); 
		localStorage.setItem('dark', !showDark) 
	}
	const sessionUser = useSelector((state) => state.session.user);
	const dispatch = useDispatch();



	useEffect(() => {
		(async () => {
			await dispatch(authenticate());
			dispatch(setTheme())
			localStorage.setItem("dark", true);  
		
			if (!localStorage.getItem("sidebar")) {
				localStorage.setItem("sidebar", true);
				setShowSidebar(true);
			} else {
				if (localStorage.getItem("sidebar") === 'false'){
					setShowSidebar(false);
				} else {
					setShowSidebar(true);
				}
			}

				setLoaded(true);


		})();
	}, [dispatch]);


	if (!loaded) {
		return (
			<div>
				<LoadingScreen />
			</div>
		)
	}
	return (
		<BrowserRouter>
			<Switch>
				<Route path="/" exact={true}>
					{!sessionUser && <Splash />}
					{sessionUser && (
						<div className="zs-main-layer">
							<SideBar show={showSidebar} toggle={toggleSidebar} toggledark={toggleDark} />
							<RootPage show={showSidebar} toggle={toggleSidebar} page="home"/>
						</div>
					)}
				</Route>
				<ProtectedRoute path="/projects/:projectId">
					<div className="zs-main-layer">
						<SideBar show={showSidebar} toggle={toggleSidebar} />
						<RootPage show={showSidebar} toggle={toggleSidebar} page="single-project" />
					</div>
				</ProtectedRoute>
				<Route path="/login" exact={true}>
					<LoginForm />
				</Route>
				<Route path="/sign-up" exact={true}>
					<SignUpForm />
				</Route>
			</Switch>
		</BrowserRouter>
	);
}

export default App;
