var app = angular.module('agenda', []);
app.controller('ContatoController', function ($scope, $http) {


    $scope.pessoa = {
        "id": "",
        "nome": "",
        "email": "",
    };

    $scope.btnDeletarVisible = false;

    $scope.salvar = function () {

        if (isNullOrEmpty($scope.pessoa.nome)) {
            alert("digite um nome")
            return
        }

        if (isNullOrEmpty($scope.pessoa.email)) {
            alert("digite um email")
            return
        }

        $http({
            method: "POST",
            url: "/api/edit",
            data: $scope.pessoa

        }).then(function mySuccess(response) {
            var x = response.data;
            $scope.pessoa.id = x.id;
            location.reload(true);
            alert("salvo com sucesso")
        }, function myError(response) {
            $scope.response = response.statusText;
        });

    }

    $http.get("/api/list")
        .then(function (response) {
            var a = response.data;
            $scope.lista = a;
        });



    $scope.addTelefone = function () {

        if (!isNullOrEmpty($scope.idPessoa)) {

            if ($scope.numemroTelefone == null ||
                $scope.numemroTelefone == "" ||
                $scope.numemroTelefone == undefined) {
                alert("digite um numero de telefone");
                return;
            }

            $http({
                method: "POST",
                url: "/api/salvarTelefone",
                data: {
                    "id": isNullOrEmpty($scope.telefoneId) ? "" : $scope.telefoneId,
                    "pessoaId": $scope.idPessoa,
                    "numero": $scope.numemroTelefone
                }
            }).then(function mySuccess(response) {
                var x = response.data;
                $scope.resetProps();
                alert(x)
            }, function myError(response) {
                $scope.response = response.statusText;
            });

            $http.get("/api/getListPhoneByUserId/" + $scope.idPessoa)
                .then(function (response) {
                    var a = response.data;
                    $scope.telefones = a;
                });
        } else {
            alert("cadastre uma pessoa primeiro")
        }
    }

    $scope.deletarContato = function () {
        var id = $scope.idPessoa.trim();
        $http({
            method: "POST",
            url: "/api/deletePessoa",
            data: {
                "id": id,               
            }
        }).then(function mySuccess(response) {
            var x = response.data;
            $scope.resetProps();
            alert(x)
            location.reload(true);
        }, function myError(response) {
            $scope.response = response.statusText;
        });
    }

    $scope.addEndereco = function () {
        if (!isNullOrEmpty($scope.idPessoa)) {

            if (isNullOrEmpty($scope.rua)) {
                alert("digite a rua")
                return
            }
            if (isNullOrEmpty($scope.cep)) {
                alert("digite o cep")
                return
            }
            if (isNullOrEmpty($scope.numero)) {
                alert("digite o numero")
                return
            }

            $http({
                method: "POST",
                url: "/api/saveEndereco",
                data: {
                    "id": isNullOrEmpty($scope.idEndereco) ? "" : $scope.idEndereco,
                    "pessoaId": $scope.idPessoa,
                    "numero": $scope.numero,
                    "cep": $scope.cep,
                    "rua": $scope.rua
                }
            }).then(function mySuccess(response) {
                var x = response.data;
                $scope.resetProps();
                alert(x)
            }, function myError(response) {
                $scope.response = response.statusText;
            });

            $http.get("/api/getListAddressByUserId/" + $scope.idPessoa)
                .then(function (response) {
                    var a = response.data;
                    $scope.enderecos = a;
                });

        } else {
            alert("cadastre uma pessoa primeiro")
        }
    }

    $scope.selectPessoaChange = function (item) {

        if (!isNullOrEmpty(item)) {

            var idPessoa = $scope.idPessoa.trim();

            $http.get("/api/getListPhoneByUserId/" + idPessoa)
                .then(function (response) {
                    var a = response.data;
                    $scope.telefones = a;
                });

            $http.get("/api/getListAddressByUserId/" + idPessoa)
                .then(function (response) {
                    var a = response.data;
                    $scope.enderecos = a;
                });


            $http.get("/api/buscaPessoaPorId/" + idPessoa)
                .then(function (response) {
                    var a = response.data;
                    $scope.pessoa = a;
                    $scope.btnDeletarVisible = true;
                });
            
        }


    }

    $scope.excluirEndereco = function (enderecoId) {

        var idPessoa = $scope.idPessoa.trim();

        $http({
            method: "POST",
            url: "/api/deleteEndereco",
            data: {
                "pessoaId": idPessoa,
                "enderecoId": enderecoId
            }
        }).then(function mySuccess(response) {
            var x = response.data;
            $scope.resetProps();
            alert(x)
        }, function myError(response) {
            $scope.response = response.statusText;
        });

        $http.get("/api/getListAddressByUserId/" + idPessoa)
            .then(function (response) {
                var a = response.data;
                $scope.enderecos = a;
            });
    }

    $scope.excluirTelefone = function (telefoneId) {

        var idPessoa = $scope.idPessoa.trim();

        $http({
            method: "POST",
            url: "/api/deleteTelefone",
            data: {
                "pessoaId": idPessoa,
                "telefoneId": telefoneId
            }
        }).then(function mySuccess(response) {
            var x = response.data;
            $scope.resetProps();
            alert(x)
        }, function myError(response) {
            $scope.response = response.statusText;
        });

        $http.get("/api/getListPhoneByUserId/" + idPessoa)
            .then(function (response) {
                var a = response.data;
                $scope.telefones = a;
            });
    }


    $scope.buscarCep = function (cep) {

        $http.get("https://viacep.com.br/ws/" + cep + "/json/")
            .then(function (response) {
                $scope.rua = response.data.logradouro;
                $scope.cep = response.data.cep.replace("-","");
            });


    }

    $scope.carregaTelefone = function (telefone) {
        $scope.numemroTelefone = telefone.numero;
        $scope.telefoneId = telefone.id;
    }

    $scope.carregaEndereco = function (endereco) {
        $scope.rua = endereco.rua;
        $scope.cep = endereco.cep;
        $scope.numero = endereco.numero;
        $scope.idEndereco = endereco.id;
    }

 

    $scope.resetProps = function () {
        $scope.numero = null;
        $scope.cep = null;
        $scope.rua = null;
        $scope.numemroTelefone = null;
        $scope.pessoa.id = null;
        $scope.pessoa.nome = null;
        $scope.pessoa.email = null;
        $scope.btnDeletarVisible = false;

    }

    function isNullOrEmpty(item) {
        if (item == "" || item == null || item == undefined) {
            return true;
        }
        return false;
    }

});