package cs320.finals;

import java.io.IOException;
import java.sql.Connection;
import java.sql.Driver;
import java.sql.DriverManager;
import java.sql.Statement;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@WebServlet("/Final/RemoveQuotation")
public class RemoveQuotation extends HttpServlet {
	private static final long serialVersionUID = 1L;
    
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException 
	{
		if(request.getParameter("quote") == null)
		{
			response.sendRedirect("/cs320stu02/Final/QuoteAdmin");
			return;
		}
		
		String theQuote = request.getParameter("quote");
		
		String username = "cs320stu02";
		String password = "HW*hR#.O";
				
		String host = "cs3.calstatela.edu";
		String port = "3306";
		String dbName = "cs320stu02";
		
		String url = "jdbc:mysql://" + host + ":" + port + "/" + dbName;
		
		try
		{
			//Dynamically include MYSQL driver
			System.out.println("Class.forName");
			Class.forName("org.gjt.mm.mysql.Driver").newInstance();
			
			//Instantiate the Driver
			Driver driver = new org.gjt.mm.mysql.Driver();
			
			//Connect to the Database
			System.out.println("Creating Connection");
			Connection connection = DriverManager.getConnection(url, username, password);
			
			//Create statement
			System.out.println("Creating Statement");
			Statement statement = connection.createStatement();
			
			//Create SQL query
			String query = "DELETE FROM quotes WHERE quote = '" + theQuote + "'";
			
			//Execute query
			int resultSet = statement.executeUpdate(query);
						
			//Tidy up
			connection.close();
			
			//Forward the request and response to the view
			System.out.println("Dispatching");
			response.sendRedirect("/cs320stu02/Final/QuoteAdmin");
		}
		
		catch(Exception e)
		{
			System.out.println(e.getLocalizedMessage());
		}
	}

	
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException 
	{
		doGet(request, response);
	}

}
