package com.javatpoint.lola;
import java.sql.*;
import java.util.*;

import com.javatpoint.bean.Baby;


public class BabyLola {

	public static Connection getCon(){
		Connection con=null;
		try{
			Class.forName("com.mysql.jdbc.Driver");
			con=DriverManager.getConnection("jdbc:mysql://localhost:3306/test","","");
		}catch(Exception e){System.out.println(e);}
		return con;
	}
	
	public static int save(Baby b){
		int status=0;
		try{
			Connection con=getCon();
			PreparedStatement ps=con.prepareStatement("insert into babyname(name,meaning,sex,religion) values(?,?,?,?)");
			ps.setString(1,b.getName());
			ps.setString(2,b.getMeaning());
			ps.setString(3,b.getSex());
			ps.setString(4,b.getReligion());
			status=ps.executeUpdate();
			con.close();
		}catch(Exception e){System.out.println(e);}
		return status;
	}
	public static int delete(int id){
		int status=0;
		try{
			Connection con=getCon();
			PreparedStatement ps=con.prepareStatement("delete from babyname where id=?");
			ps.setInt(1,id);
			status=ps.executeUpdate();
			con.close();
		}catch(Exception e){System.out.println(e);}
		return status;
	}
	public static List<Baby> getAllRecords(){
		List<Baby> list=new ArrayList<Baby>();
		try{
			Connection con=getCon();
			PreparedStatement ps=con.prepareStatement("select * from babyname");
			ResultSet rs=ps.executeQuery();
			while(rs.next()){
				Baby b=new Baby();
				b.setId(rs.getInt(1));
				b.setName(rs.getString(2));
				b.setMeaning(rs.getString(3));
				b.setSex(rs.getString(4));
				b.setReligion(rs.getString(5));
				list.add(b);
			}
			con.close();
		}catch(Exception e){System.out.println(e);}
		return list;
	}
	public static List<Baby> getRecordsByStart(String start){
		List<Baby> list=new ArrayList<Baby>();
		try{
			Connection con=getCon();
			PreparedStatement ps=con.prepareStatement("select * from babyname where name like '"+start+"%' ");
			ResultSet rs=ps.executeQuery();
			while(rs.next()){
				Baby b=new Baby();
				b.setId(rs.getInt(1));
				b.setName(rs.getString(2));
				b.setMeaning(rs.getString(3));
				b.setSex(rs.getString(4));
				b.setReligion(rs.getString(5));
				list.add(b);
			}
			con.close();
		}catch(Exception e){System.out.println(e);}
		return list;
	}
	public static List<Baby> getRecordsByReligion(String religion){
		List<Baby> list=new ArrayList<Baby>();
		try{
			Connection con=getCon();
			PreparedStatement ps=con.prepareStatement("select * from babyname where religion=? ");
			ps.setString(1,religion);
			ResultSet rs=ps.executeQuery();
			while(rs.next()){
				Baby b=new Baby();
				b.setId(rs.getInt(1));
				b.setName(rs.getString(2));
				b.setMeaning(rs.getString(3));
				b.setSex(rs.getString(4));
				b.setReligion(rs.getString(5));
				list.add(b);
			}
			con.close();
		}catch(Exception e){System.out.println(e);}
		return list;
	}
}
