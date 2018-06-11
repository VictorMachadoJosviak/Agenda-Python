var app = angular.module('agenda', []);
app.controller('HomeController', function ($scope,$http) {

    $http.get("/api/list")
        .then(function (response) {
            var a = response.data;
            $scope.lista = a;
            console.log($scope.lista)
        });


    $scope.deletarContato = function (pessoa) {
    
        $http({
            method: "POST",
            url: "/api/deletePessoa",
            data: {
                "id": pessoa.id,
            }
        }).then(function mySuccess(response) {
            var x = response.data;
            alert(x)
            location.reload(true);
        }, function myError(response) {
            $scope.response = response.statusText;
        });
    }
    
});