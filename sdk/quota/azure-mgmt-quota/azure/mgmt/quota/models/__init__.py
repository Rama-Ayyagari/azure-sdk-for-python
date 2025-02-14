# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import CommonResourceProperties
    from ._models_py3 import CreateGenericQuotaRequestParameters
    from ._models_py3 import CurrentQuotaLimitBase
    from ._models_py3 import CurrentUsagesBase
    from ._models_py3 import ExceptionResponse
    from ._models_py3 import LimitJsonObject
    from ._models_py3 import LimitObject
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationList
    from ._models_py3 import OperationResponse
    from ._models_py3 import QuotaLimits
    from ._models_py3 import QuotaLimitsResponse
    from ._models_py3 import QuotaProperties
    from ._models_py3 import QuotaRequestDetails
    from ._models_py3 import QuotaRequestDetailsList
    from ._models_py3 import QuotaRequestOneResourceSubmitResponse
    from ._models_py3 import QuotaRequestProperties
    from ._models_py3 import QuotaRequestSubmitResponse
    from ._models_py3 import QuotaRequestSubmitResponse202
    from ._models_py3 import ResourceName
    from ._models_py3 import ServiceError
    from ._models_py3 import ServiceErrorDetail
    from ._models_py3 import SubRequest
    from ._models_py3 import UsagesLimits
    from ._models_py3 import UsagesObject
    from ._models_py3 import UsagesProperties
except (SyntaxError, ImportError):
    from ._models import CommonResourceProperties  # type: ignore
    from ._models import CreateGenericQuotaRequestParameters  # type: ignore
    from ._models import CurrentQuotaLimitBase  # type: ignore
    from ._models import CurrentUsagesBase  # type: ignore
    from ._models import ExceptionResponse  # type: ignore
    from ._models import LimitJsonObject  # type: ignore
    from ._models import LimitObject  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationList  # type: ignore
    from ._models import OperationResponse  # type: ignore
    from ._models import QuotaLimits  # type: ignore
    from ._models import QuotaLimitsResponse  # type: ignore
    from ._models import QuotaProperties  # type: ignore
    from ._models import QuotaRequestDetails  # type: ignore
    from ._models import QuotaRequestDetailsList  # type: ignore
    from ._models import QuotaRequestOneResourceSubmitResponse  # type: ignore
    from ._models import QuotaRequestProperties  # type: ignore
    from ._models import QuotaRequestSubmitResponse  # type: ignore
    from ._models import QuotaRequestSubmitResponse202  # type: ignore
    from ._models import ResourceName  # type: ignore
    from ._models import ServiceError  # type: ignore
    from ._models import ServiceErrorDetail  # type: ignore
    from ._models import SubRequest  # type: ignore
    from ._models import UsagesLimits  # type: ignore
    from ._models import UsagesObject  # type: ignore
    from ._models import UsagesProperties  # type: ignore

from ._azure_quota_extension_api_enums import (
    LimitType,
    QuotaLimitTypes,
    QuotaRequestState,
    UsagesTypes,
)

__all__ = [
    'CommonResourceProperties',
    'CreateGenericQuotaRequestParameters',
    'CurrentQuotaLimitBase',
    'CurrentUsagesBase',
    'ExceptionResponse',
    'LimitJsonObject',
    'LimitObject',
    'OperationDisplay',
    'OperationList',
    'OperationResponse',
    'QuotaLimits',
    'QuotaLimitsResponse',
    'QuotaProperties',
    'QuotaRequestDetails',
    'QuotaRequestDetailsList',
    'QuotaRequestOneResourceSubmitResponse',
    'QuotaRequestProperties',
    'QuotaRequestSubmitResponse',
    'QuotaRequestSubmitResponse202',
    'ResourceName',
    'ServiceError',
    'ServiceErrorDetail',
    'SubRequest',
    'UsagesLimits',
    'UsagesObject',
    'UsagesProperties',
    'LimitType',
    'QuotaLimitTypes',
    'QuotaRequestState',
    'UsagesTypes',
]
