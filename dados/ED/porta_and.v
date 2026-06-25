// ==========================================
// 1. O CIRCUITO (O que vai para a FPGA)
// ==========================================
module porta_and (
    input wire A,   // Fio de entrada A
    input wire B,   // Fio de entrada B
    output wire S   // Fio de saída S
);
    
    // A palavra 'assign' significa uma ligação física contínua. 
    // "Fie o pino S na saída de uma porta AND (&) entre A e B"
    assign S = A & B; 

endmodule

// ==========================================
// 2. O TESTBENCH (Para simular no computador)
// ==========================================
module tb_porta_and;

    // No testbench, ENTRADAS viram 'reg' (registradores que seguram um valor que nós vamos mudar)
    reg tb_A;
    reg tb_B;
    // SAÍDAS viram 'wire' (fios para apenas lermos o resultado)
    wire tb_S;

    // Conectando o nosso testbench no circuito que criamos lá em cima
    porta_and meucircuito (
        .A(tb_A),
        .B(tb_B),
        .S(tb_S)
    );

    // O bloco 'initial' executa uma única vez, de cima para baixo. (Não é sintetizável na placa real)
    initial begin
        // Comandos mágicos para gerar o arquivo pro GTKWave ler depois
        $dumpfile("ondas.vcd");
        $dumpvars(0, tb_porta_and);

        // Testando a tabela verdade:
        tb_A = 0; tb_B = 0; #10; // '#10' significa: "espere 10 unidades de tempo"
        tb_A = 0; tb_B = 1; #10;
        tb_A = 1; tb_B = 0; #10;
        tb_A = 1; tb_B = 1; #10;

        $display("Teste finalizado com sucesso!");
        $finish; // Encerra a simulação
    end

endmodule