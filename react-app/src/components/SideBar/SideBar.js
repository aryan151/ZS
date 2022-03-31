import React from "react";
import { NavLink, Link } from "react-router-dom";
import { useSelector } from "react-redux";
import LogoutButton from "../auth/LogoutButton";
import { BsLinkedin, BsGithub } from "react-icons/bs";
import NewProject from "./NewProject";
import { MdMenuOpen } from "react-icons/md";
import { FaSquare, FaPlus } from "react-icons/fa";
import OpenBoardLogo from "../../images/OpenBoard-Logo-Dark.png";
import "./SideBar.css";
import { MdHome} from "react-icons/md";

const SideBar = ({ show, toggle }) => {
	const user = useSelector((state) => state.session.user);
	const user_projects = user.projects;
	const sidebarClass = show ? "sidebar-open" : "sidebar-closed";

	return (
		<nav className={sidebarClass}>
			<div className="sidebar-header">
				<p id="sidebar-header-logo">Navigation</p> 
				<div id="sidebar-toggle-button" onClick={toggle}>
					<MdMenuOpen size="2em" />
				</div>
			</div>
			<div className="sidebar-links-section">
				<NavLink to="/" exact={true} activeClassName="sidebar-active">
					<div id="sidebar-link">
						<MdHome size="1.5em" className='sidebarlogotopleft' /> <span id="sidebar-link-text">Home</span>
					</div>
				</NavLink>
			</div>
			<div className="sidebar-projects-section">
				<div id="sidebar-projects-title">
					My Projects <div id="add-project-button"> <NewProject location="sidebar" /></div>
				</div>
				{user_projects
					? Object.keys(user_projects).map((key) => (
							<NavLink
								activeClassName="sidebar-active"
								key={user_projects[key].project_id}
								to={`/projects/${user_projects[key].project_id}`}
							>
								<div id="sidebar-project-link">
									<div id="sidebar-project-color">
										<FaSquare
											size=".7em"
											color={user_projects[key].project_color}
										/>
									</div>
									<div id="sidebar-project-link-title">
										{user_projects[key].project_title}
									</div>
								</div>
							</NavLink>
					  ))
					: null}
			</div>
			<div className="sidebar-log-out">
				<LogoutButton />
			</div> 
		</nav>
	);
};

export default SideBar;
