package cs320.finals;

import java.io.IOException;
import java.sql.Connection;
import java.sql.Driver;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Random;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@WebServlet("/Final/QuoteAdmin")
public class AdminView extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
   
    
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException 
	{
		
		
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
			String query = "SELECT * FROM quotes";
			
			//Execute query
			ResultSet resultSet = statement.executeQuery(query);
			
			//Iterate over the results, and create models for the view
			ArrayList<Quotation> quotes = new ArrayList<Quotation>();
			
			System.out.println("Iterating over results");
			
			
			
				while(resultSet.next())
				{
					String author = resultSet.getString("author");
					String quote = resultSet.getString("quote");
					int timesViewed = resultSet.getInt("timesViewed");
					quotes.add(new Quotation(author, quote, timesViewed));
				}
				
			
					
			
			//Tidy up
			connection.close();
			
			//Attach the results to the Request object
			request.setAttribute("quotes", quotes);
			
			//Forward the request and response to the view
			System.out.println("Dispatching");
			request.getRequestDispatcher("/WEB-INF/final/AdminView.jsp").forward(request, response);
		}
		
		catch(Exception e)
		{
			System.out.println(e.getLocalizedMessage());
		}
	}

	
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException 
	{
		if(request.getParameter("author") == "" || request.getParameter("quote") == "")
		{
			response.sendRedirect("/cs320stu02/Final/QuoteAdmin");
			return;
		}
		
		String newAuthor = request.getParameter("author");
		String newQuote = request.getParameter("quote");
		
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
			String query = "INSERT INTO quotes VALUES ('" + newAuthor + "','" + newQuote + "','" + "0" + "')";
			
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

}
