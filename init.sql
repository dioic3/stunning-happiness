CREATE DATABASE IF NOT EXISTS quiz;
USE quiz;
CREATE TABLE questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT,
    option_a VARCHAR(255),
    option_b VARCHAR(255),
    option_c VARCHAR(255),
    option_d VARCHAR(255),
    correct_answer CHAR(1)
);
SELECT * FROM questions LIMIT 10;
INSERT INTO questions (question, option_a, option_b, option_c, option_d, correct_answer) 
VALUES 
('Qual é a capital do Brasil?', 'Buenos Aires', 'Rio de Janeiro', 'São Paulo', 'Brasília', 'd'),
('Qual é a capital do Japão?', 'Beijing', 'Seoul', 'Tokyo', 'Shanghai', 'c'),
('Qual é a capital da Rússia?', 'Moscou', 'São Petersburgo', 'Kiev', 'Vladivostok', 'a'),
('Qual é a capital da Austrália?', 'Sydney', 'Melbourne', 'Canberra', 'Brisbane', 'c');





