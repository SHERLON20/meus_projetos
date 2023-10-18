/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package sistema_login.core.DAO.conexao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import javax.swing.JOptionPane;

/**
 *
 * @author sherl
 */
public class conexaojdbc {
    private static final String URL="jdbc:mysql://localhost:3306/mapa";
    private static final String USER="root";
    private static final String PASSWORD="sherlon21";
    
    public static Connection conn;

    public static Connection getconexao(){
        try{
            if (conn == null){
                conn = DriverManager.getConnection(URL, USER, PASSWORD);
                return conn;
            }else{
                return conn;
            }
        
        
        }catch (SQLException e ){
            JOptionPane.showMessageDialog(null, "houve um erro ao tentar fazer a conexão.");
            return null;
        }
        
    }
}
