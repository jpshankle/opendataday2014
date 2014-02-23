var app = angular.module('stopcorruption', ['ngRoute', 'ngResource']);

app.config(['$routeProvider', function ($routeProvider) {
    $routeProvider
		.when('/', {
			controller: 'HomeCtrl',
			templateUrl: 'home.html'
		})
        .when('/source/:source', {
            controller: 'ImportSourceCtrl',
            templateUrl: 'import-source.html'
		})
    .otherwise({
        redirectTo: '/'
	});
}]);

app.factory('SourceResource', ['$resource', function ($resource) {
	return $resource('/api/source/:id');
}]);

app.controller('HomeCtrl', ['$scope', '$http', '$resource', 'SourceResource', function ($scope, $http, $resource, SourceResource) {
    $scope.importSources = SourceResource.query(function () {
        $scope.importSources.forEach(function(i) {
            i.id = i._id.$oid;
        });
    });
    $scope.importButton = function() {
		$http.post('/api/import', { things: 'all' })
			.success(function () {
				console.log(arguments[0]);
			});
    };
}]);

app.controller('ImportSourceCtrl', ['$scope', 'SourceResource', '$routeParams', '$location', function ($scope, SourceResource, $routeParams, $location) {
	if ($routeParams.source === 'add') {
		$scope.importSource = new SourceResource({
			field_mappings: [],
            source_type: '',
            name: '',
			url: '',
            country: '',
            region: '',
            language: '',
            currency: ''
		});
	} else {
		$scope.importSource = SourceResource.get({
			importSource: $routeParams.source
		});
	}
	$scope.addMapping = function (selectedMapping) {
		$scope.importSource.field_mappings.push({
			source_field: '',
			dest_field: selectedMapping
		});
    };
    $scope.saveSource = function () {
        $scope.importSource.$save(function () {
            $location.path('/');
        });
    };

    $scope.possibleSourceTypes = [
        'json',
        'worldbank_json'
    ];

    $scope.possibleMappings = [
        'source',
        'project_name',
        'description',
        'procument_method',
        'procument_category',
        'organization',
        'sector',
        'supplier',
        'supplier_country',
        'fiscal_year',
        'contract_signed',
        'tender_issued',
        'region',
        'date',
        'amount'
    ];
}]);