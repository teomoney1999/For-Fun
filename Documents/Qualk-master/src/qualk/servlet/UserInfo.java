package qualk.servlet;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import qualk.beans.*;
import qualk.utils.*;

@WebServlet("/userinfo")
public class UserInfo extends HttpServlet{
	
	private static final long serialVersionUID = 1L; 
	
	protected void doGet(HttpServletRequest req, HttpServletResponse resp)
		throws ServletException, IOException{
		
		HttpSession session = req.getSession();
		
		User loginedUser = MyUtils.getLoginedUser(session);
		
		// Not login yet
		if (loginedUser == null) {
			resp.sendRedirect("/WEB-INF/jobfinder/login.jsp");
			return;
		}
		
		// Store information in request attribute before forward

		req.setAttribute("user", loginedUser);
		RequestDispatcher dispatcher = this.getServletContext().getRequestDispatcher("/WEB-INF/jobfinder/userLoginInfo.jsp");
		dispatcher.forward(req, resp); 
	}
	
	protected void doPost(HttpServletRequest req, HttpServletResponse resp)
			throws ServletException, IOException{
		doGet(req, resp);
	}
}
