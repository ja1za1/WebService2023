package wbs.entities;


public class Turma {
	private String id,nome;
	private int ano;
	private Aluno[] alunos;
	private Aluno lider;
	
	
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public int getAno() {
		return ano;
	}
	public void setAno(int ano) {
		this.ano = ano;
	}
	public Aluno[] getAlunos() {
		return alunos;
	}
	public void setAlunos(Aluno[] alunos) {
		this.alunos = alunos;
	}
	
	public Aluno getLider() {
		return lider;
	}
	public void setLider(Aluno lider) {
		this.lider = lider;
	}
	@Override
	public String toString() {
		
		StringBuilder relatorioTurma = new StringBuilder();
		relatorioTurma.append(String.format("%s (%d)\n", this.nome,this.ano));
		if(alunos != null) {
			for(Aluno aluno : alunos) {
				relatorioTurma.append(aluno.toString());
			}
		}
		
		return relatorioTurma.toString();
	}
	
	
	
	
}
