/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package sistema_login.core.DAO;
import java.sql.Connection;
import java.sql.ResultSet;
import sistema_login.core.DAO.conexao.conexaojdbc;
import sistema_login.core.entity.login.login;
import java.sql.SQLException;
import javax.swing.JOptionPane;
import java.sql.PreparedStatement;
/**
 *
 * @author sherl
 */
public class loginDAO {
    Connection conn;
    
    public ResultSet autenticacao(login l){
        conn = new conexaojdbc().getconexao();
        try {
            String sql=" SELECT id, nome, login, senha , email from usuario where login = ? and senha = ?";
            PreparedStatement ps = conn.prepareStatement(sql);
            ps.setString(1, l.getLogin());
            ps.setString(2, l.getSenha());
            ResultSet rs = ps.executeQuery();
            return rs;
            
        }catch(SQLException e) {
            JOptionPane.showMessageDialog(null, "erro ao buscar o banco");
            return null;
        }
        
    }
}
