/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package sistema_login.core.DAO;

import sistema_login.core.entity.cadastro;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import sistema_login.core.DAO.conexao.conexaojdbc;


/**
 *
 * @author sherl
 */
public class cadastroDAO{
    
    public void inserir(cadastro c) {
        String sql="insert into usuario(nome, login, senha, email) values (?,?,?,?)";
        PreparedStatement ps;
        try{
            ps = conexaojdbc.getconexao().prepareStatement(sql);
            ps.setString(1,c.getNome());
            ps.setString(2, c.getLogin());
            ps.setString(3, c.getSenha());
            ps.setString(4, c.getEmail());
            
            ps.execute();
        }catch(SQLException e){
            e.printStackTrace();
        
        }
        }
  

}
