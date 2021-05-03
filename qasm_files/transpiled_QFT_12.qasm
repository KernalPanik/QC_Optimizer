OPENQASM 2.0;
include "qelib1.inc";
qreg q[12];
u1(pi/4096) q[0];
u1(pi/2048) q[1];
u1(pi/1024) q[2];
u1(pi/512) q[3];
u1(pi/256) q[4];
u1(pi/128) q[5];
u1(pi/64) q[6];
u1(pi/32) q[7];
u1(pi/16) q[8];
u1(pi/8) q[9];
u1(pi/4) q[10];
u2(0,pi) q[11];
cx q[0],q[11];
u1(-pi/4096) q[11];
cx q[0],q[11];
u1(pi/2048) q[0];
u1(pi/4096) q[11];
cx q[1],q[11];
u1(-pi/2048) q[11];
cx q[1],q[11];
u1(pi/1024) q[1];
u1(pi/2048) q[11];
cx q[2],q[11];
u1(-pi/1024) q[11];
cx q[2],q[11];
u1(pi/1024) q[11];
u1(pi/512) q[2];
cx q[3],q[11];
u1(-pi/512) q[11];
cx q[3],q[11];
u1(pi/512) q[11];
u1(pi/256) q[3];
cx q[4],q[11];
u1(-pi/256) q[11];
cx q[4],q[11];
u1(pi/256) q[11];
u1(pi/128) q[4];
cx q[5],q[11];
u1(-pi/128) q[11];
cx q[5],q[11];
u1(pi/128) q[11];
u1(pi/64) q[5];
cx q[6],q[11];
u1(-pi/64) q[11];
cx q[6],q[11];
u1(pi/64) q[11];
u1(pi/32) q[6];
cx q[7],q[11];
u1(-pi/32) q[11];
cx q[7],q[11];
u1(pi/32) q[11];
u1(pi/16) q[7];
cx q[8],q[11];
u1(-pi/16) q[11];
cx q[8],q[11];
u1(pi/16) q[11];
u1(pi/8) q[8];
cx q[9],q[11];
u1(-pi/8) q[11];
cx q[9],q[11];
u1(pi/8) q[11];
cx q[10],q[11];
u1(-pi/4) q[11];
cx q[10],q[11];
u2(0,pi) q[10];
cx q[0],q[10];
u1(-pi/2048) q[10];
cx q[0],q[10];
u1(pi/1024) q[0];
u1(pi/2048) q[10];
cx q[1],q[10];
u1(-pi/1024) q[10];
cx q[1],q[10];
u1(pi/512) q[1];
u1(pi/1024) q[10];
u1(pi/4) q[11];
cx q[2],q[10];
u1(-pi/512) q[10];
cx q[2],q[10];
u1(pi/512) q[10];
u1(pi/256) q[2];
cx q[3],q[10];
u1(-pi/256) q[10];
cx q[3],q[10];
u1(pi/256) q[10];
u1(pi/128) q[3];
cx q[4],q[10];
u1(-pi/128) q[10];
cx q[4],q[10];
u1(pi/128) q[10];
u1(pi/64) q[4];
cx q[5],q[10];
u1(-pi/64) q[10];
cx q[5],q[10];
u1(pi/64) q[10];
u1(pi/32) q[5];
cx q[6],q[10];
u1(-pi/32) q[10];
cx q[6],q[10];
u1(pi/32) q[10];
u1(pi/16) q[6];
cx q[7],q[10];
u1(-pi/16) q[10];
cx q[7],q[10];
u1(pi/16) q[10];
u1(pi/8) q[7];
cx q[8],q[10];
u1(-pi/8) q[10];
cx q[8],q[10];
u1(pi/8) q[10];
u1(pi/4) q[8];
u1(pi/4) q[9];
cx q[9],q[10];
u1(-pi/4) q[10];
cx q[9],q[10];
u1(pi/4) q[10];
u2(0,pi) q[9];
cx q[0],q[9];
u1(-pi/1024) q[9];
cx q[0],q[9];
u1(pi/512) q[0];
u1(pi/1024) q[9];
cx q[1],q[9];
u1(-pi/512) q[9];
cx q[1],q[9];
u1(pi/256) q[1];
u1(pi/512) q[9];
cx q[2],q[9];
u1(-pi/256) q[9];
cx q[2],q[9];
u1(pi/128) q[2];
u1(pi/256) q[9];
cx q[3],q[9];
u1(-pi/128) q[9];
cx q[3],q[9];
u1(pi/64) q[3];
u1(pi/128) q[9];
cx q[4],q[9];
u1(-pi/64) q[9];
cx q[4],q[9];
u1(pi/32) q[4];
u1(pi/64) q[9];
cx q[5],q[9];
u1(-pi/32) q[9];
cx q[5],q[9];
u1(pi/16) q[5];
u1(pi/32) q[9];
cx q[6],q[9];
u1(-pi/16) q[9];
cx q[6],q[9];
u1(pi/8) q[6];
u1(pi/16) q[9];
cx q[7],q[9];
u1(-pi/8) q[9];
cx q[7],q[9];
u1(pi/4) q[7];
u1(pi/8) q[9];
cx q[8],q[9];
u1(-pi/4) q[9];
cx q[8],q[9];
u2(0,pi) q[8];
cx q[0],q[8];
u1(-pi/512) q[8];
cx q[0],q[8];
u1(pi/256) q[0];
u1(pi/512) q[8];
cx q[1],q[8];
u1(-pi/256) q[8];
cx q[1],q[8];
u1(pi/128) q[1];
u1(pi/256) q[8];
cx q[2],q[8];
u1(-pi/128) q[8];
cx q[2],q[8];
u1(pi/64) q[2];
u1(pi/128) q[8];
cx q[3],q[8];
u1(-pi/64) q[8];
cx q[3],q[8];
u1(pi/32) q[3];
u1(pi/64) q[8];
cx q[4],q[8];
u1(-pi/32) q[8];
cx q[4],q[8];
u1(pi/16) q[4];
u1(pi/32) q[8];
cx q[5],q[8];
u1(-pi/16) q[8];
cx q[5],q[8];
u1(pi/8) q[5];
u1(pi/16) q[8];
cx q[6],q[8];
u1(-pi/8) q[8];
cx q[6],q[8];
u1(pi/4) q[6];
u1(pi/8) q[8];
cx q[7],q[8];
u1(-pi/4) q[8];
cx q[7],q[8];
u2(0,pi) q[7];
cx q[0],q[7];
u1(-pi/256) q[7];
cx q[0],q[7];
u1(pi/128) q[0];
u1(pi/256) q[7];
cx q[1],q[7];
u1(-pi/128) q[7];
cx q[1],q[7];
u1(pi/64) q[1];
u1(pi/128) q[7];
cx q[2],q[7];
u1(-pi/64) q[7];
cx q[2],q[7];
u1(pi/32) q[2];
u1(pi/64) q[7];
cx q[3],q[7];
u1(-pi/32) q[7];
cx q[3],q[7];
u1(pi/16) q[3];
u1(pi/32) q[7];
cx q[4],q[7];
u1(-pi/16) q[7];
cx q[4],q[7];
u1(pi/8) q[4];
u1(pi/16) q[7];
cx q[5],q[7];
u1(-pi/8) q[7];
cx q[5],q[7];
u1(pi/4) q[5];
u1(pi/8) q[7];
cx q[6],q[7];
u1(-pi/4) q[7];
cx q[6],q[7];
u2(0,pi) q[6];
cx q[0],q[6];
u1(-pi/128) q[6];
cx q[0],q[6];
u1(pi/64) q[0];
u1(pi/128) q[6];
cx q[1],q[6];
u1(-pi/64) q[6];
cx q[1],q[6];
u1(pi/32) q[1];
u1(pi/64) q[6];
cx q[2],q[6];
u1(-pi/32) q[6];
cx q[2],q[6];
u1(pi/16) q[2];
u1(pi/32) q[6];
cx q[3],q[6];
u1(-pi/16) q[6];
cx q[3],q[6];
u1(pi/8) q[3];
u1(pi/16) q[6];
cx q[4],q[6];
u1(-pi/8) q[6];
cx q[4],q[6];
u1(pi/4) q[4];
u1(pi/8) q[6];
cx q[5],q[6];
u1(-pi/4) q[6];
cx q[5],q[6];
u2(0,pi) q[5];
cx q[0],q[5];
u1(-pi/64) q[5];
cx q[0],q[5];
u1(pi/32) q[0];
u1(pi/64) q[5];
cx q[1],q[5];
u1(-pi/32) q[5];
cx q[1],q[5];
u1(pi/16) q[1];
u1(pi/32) q[5];
cx q[2],q[5];
u1(-pi/16) q[5];
cx q[2],q[5];
u1(pi/8) q[2];
u1(pi/16) q[5];
cx q[3],q[5];
u1(-pi/8) q[5];
cx q[3],q[5];
u1(pi/4) q[3];
u1(pi/8) q[5];
cx q[4],q[5];
u1(-pi/4) q[5];
cx q[4],q[5];
u2(0,pi) q[4];
cx q[0],q[4];
u1(-pi/32) q[4];
cx q[0],q[4];
u1(pi/16) q[0];
u1(pi/32) q[4];
cx q[1],q[4];
u1(-pi/16) q[4];
cx q[1],q[4];
u1(pi/8) q[1];
u1(pi/16) q[4];
cx q[2],q[4];
u1(-pi/8) q[4];
cx q[2],q[4];
u1(pi/4) q[2];
u1(pi/8) q[4];
cx q[3],q[4];
u1(-pi/4) q[4];
cx q[3],q[4];
u2(0,pi) q[3];
cx q[0],q[3];
u1(-pi/16) q[3];
cx q[0],q[3];
u1(pi/8) q[0];
u1(pi/16) q[3];
cx q[1],q[3];
u1(-pi/8) q[3];
cx q[1],q[3];
u1(pi/4) q[1];
u1(pi/8) q[3];
cx q[2],q[3];
u1(-pi/4) q[3];
cx q[2],q[3];
u2(0,pi) q[2];
cx q[0],q[2];
u1(-pi/8) q[2];
cx q[0],q[2];
u1(pi/4) q[0];
u1(pi/8) q[2];
cx q[1],q[2];
u1(-pi/4) q[2];
cx q[1],q[2];
u2(0,pi) q[1];
cx q[0],q[1];
u1(-pi/4) q[1];
cx q[0],q[1];
u2(0,pi) q[0];
cx q[0],q[11];
u1(pi/4) q[1];
cx q[1],q[10];
cx q[10],q[1];
cx q[1],q[10];
cx q[11],q[0];
cx q[0],q[11];
u1(pi/4) q[2];
u1(pi/4) q[3];
u1(pi/4) q[4];
u1(pi/4) q[5];
u1(pi/4) q[6];
cx q[5],q[6];
cx q[6],q[5];
cx q[5],q[6];
u1(pi/4) q[7];
cx q[4],q[7];
cx q[7],q[4];
cx q[4],q[7];
u1(pi/4) q[8];
cx q[3],q[8];
cx q[8],q[3];
cx q[3],q[8];
u1(pi/4) q[9];
cx q[2],q[9];
cx q[9],q[2];
cx q[2],q[9];
