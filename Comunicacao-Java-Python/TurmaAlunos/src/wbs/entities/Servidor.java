package wbs.entities;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.google.gson.Gson;

public class Servidor {

	public static void main(String[] args) {
		Turma turmaWbs = new Turma();
		turmaWbs.setAno(2023);
		turmaWbs.setId("1000");
		turmaWbs.setNome("Turma WebService");
		
		Turma turmaSd = new Turma();
		turmaSd.setAno(2023);
		turmaSd.setId("2000");
		turmaSd.setNome("Turma Sistemas Distribuidos");
		
		Aluno[] alunosWbs = {new Aluno("0001","João Lucas",21),
							 new Aluno("0002", "Vitor", 21),
							 new Aluno("0003", "Caren",21),
							 new Aluno("0004", "Pedro", 22),
							 new Aluno("0005", "Vinicius", 20)
		};
		Aluno[] alunosSd = {new Aluno("0010", "Fernanda", 24),
							new Aluno("0023", "Pedro", 25),
							new Aluno("0037", "Marcela", 22),
							new Aluno("0040", "Roberto", 26),
							new Aluno("0048", "Gabriel", 22)
				
		};
		List<Turma> turmas = new ArrayList<>();
		turmaWbs.setAlunos(alunosWbs);
		turmaSd.setAlunos(alunosSd);
		turmas.add(turmaWbs);
		turmas.add(turmaSd);
		iniciarServidor(turmas);
	}

	private static void iniciarServidor(List<Turma>turmas) {
		try (ServerSocket socketServidor = new ServerSocket(37000)){
			System.out.println("Servidor ouvindo na porta 37000");
			while(true) {
				Socket cliente = socketServidor.accept();
				System.out.println("Cliente conectado: " + cliente.getInetAddress().getHostAddress());
				PrintWriter saida = new PrintWriter(cliente.getOutputStream(),true);
				String json = converterTurmasParaJson(turmas);
				saida.println(json);
				saida.println();
				BufferedReader buffer = new BufferedReader(new InputStreamReader(cliente.getInputStream()));
				String lideres = buffer.readLine();
				definirLideres(lideres, turmas);
				cliente.close();
				buffer.close();
				saida.close();
			}
			
		} catch (IOException e) {
			System.out.println("Erro: " + e.getMessage());
		}
	}
	
	private static void definirLideres(String lideres, List<Turma> turmas) {
		Aluno[] alunos_lideres = new Gson().fromJson(lideres, Aluno[].class);
		for(int i = 0; i < turmas.size(); i++) {
			turmas.get(i).setLider(alunos_lideres[i]);
		}
	}

	private static String converterTurmasParaJson(List<Turma> turmas) {
		return new Gson().toJson(turmas);
	}

}
