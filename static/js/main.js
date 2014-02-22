var app = angular.module('stopcorruption', ['ngRoute', 'ngResource']);

app.config(['$routeProvider', function ($routeProvider) {
	    $routeProvider
	    .when('/', {
		    controller: 'HomeCtrl',
		    templateUrl: 'home.html'
		})
	    .when('/import-sources', {
		    controller: 'ImportSourcesCtrl',
		    templateUrl: 'import-types.html'
		})
	    .when('/import-sources/:importSource', {
		    controller: 'ImportSourceCtrl',
		    templateUrl: 'import-type.html'
		})
	    .otherwise({
		    redirectTo: '/'
		});
}]);

app.factory('SourceResource', ['$resource', function ($resource) {
	    return $resource('/api/:id');
}]);

app.controller('HomeCtrl', ['$scope', '$http', function ($scope, $http) {
	    $scope.importButton = function() {
			$http.post('/api/import')
				.success(function () {
					console.log('success posting');
				});
	    };
}]);
app.controller('ImportSourcesCtrl', ['$scope', '$resource', 'SourceResource', function ($scope, $resource, SourceResource) {
	    $scope.importSources = SourceResource.query();
}]);
app.controller('ImportSourceCtrl', ['$scope', 'SourceResource', '$routeParams', function ($scope, SourceResource, $routeParams) {
		if ($routeParams.importSource === 'add') {
			$scope.importSource = new SourceResource({
				field_mappings: [],
				url: '',
			    country: '',
			    region: '',
			    language: '',
			    currency: ''
			});
		} else {
			$scope.importSource = SourceResource.get('/api/import-sources/' + {
				importSource: $routeParams.importSource
			});
		}
		$scope.addMapping = function (selectedMapping) {
			$scope.importSource.field_mappings.push({
				source_field: '',
				dest_field: selectedMapping
			});
	    };
	    $scope.importSource.$save(function () {
	    	$location.path('/import-sources');
	    });

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
	    ]
}]);