# Copyright (c) 2024 CRS4
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pathlib import Path
from tempfile import TemporaryDirectory

from pytest import fixture

CURRENT_PATH = Path(__file__).resolve().parent
TEST_DATA_PATH = (CURRENT_PATH / "data").absolute()
CRATES_DATA_PATH = TEST_DATA_PATH / "crates"
VALID_CRATES_DATA_PATH = CRATES_DATA_PATH / "valid"
INVALID_CRATES_DATA_PATH = CRATES_DATA_PATH / "invalid"


@fixture
def ro_crates_path() -> Path:
    return CRATES_DATA_PATH


class ValidROC:
    @property
    def wrroc_paper(self) -> Path:
        return VALID_CRATES_DATA_PATH / "wrroc-paper"

    @property
    def wrroc_paper_long_date(self) -> Path:
        return VALID_CRATES_DATA_PATH / "wrroc-paper-long-date"

    @property
    def workflow_roc(self) -> Path:
        return VALID_CRATES_DATA_PATH / "workflow-roc"

    @property
    def workflow_roc_string_license(self) -> Path:
        return VALID_CRATES_DATA_PATH / "workflow-roc-string-license"

    @property
    def sort_and_change_remote(self) -> Path:
        return "https://raw.githubusercontent.com/lifemonitor/validator-test-data/main/sortchangecase.crate.zip"

    @property
    def sort_and_change_archive(self) -> Path:
        return VALID_CRATES_DATA_PATH / "sortchangecase.crate.zip"

    @property
    def process_run_crate(self) -> Path:
        return VALID_CRATES_DATA_PATH / "process-run-crate"

    @property
    def process_run_crate_collections(self) -> Path:
        return VALID_CRATES_DATA_PATH / "process-run-crate-collections"

    @property
    def process_run_crate_containerimage(self) -> Path:
        return VALID_CRATES_DATA_PATH / "process-run-crate-containerimage"

    @property
    def workflow_testing_ro_crate(self) -> Path:
        return VALID_CRATES_DATA_PATH / "workflow-testing-ro-crate"


class InvalidFileDescriptor:

    base_path = INVALID_CRATES_DATA_PATH / "0_file_descriptor_format"

    @property
    def missing_file_descriptor(self) -> Path:
        return TemporaryDirectory()

    @property
    def invalid_json_format(self) -> Path:
        return self.base_path / "invalid_json_format"

    @property
    def invalid_jsonld_format(self) -> Path:
        return self.base_path / "invalid_jsonld_format"


class InvalidRootDataEntity:

    base_path = INVALID_CRATES_DATA_PATH / "2_root_data_entity_metadata"

    @property
    def missing_root(self) -> Path:
        return self.base_path / "missing_root_entity"

    @property
    def invalid_root_type(self) -> Path:
        return self.base_path / "invalid_root_type"

    @property
    def invalid_root_value(self) -> Path:
        return self.base_path / "invalid_root_value"

    @property
    def recommended_root_value(self) -> Path:
        return self.base_path / "recommended_root_value"

    @property
    def invalid_root_date(self) -> Path:
        return self.base_path / "invalid_root_date"

    @property
    def missing_root_name(self) -> Path:
        return self.base_path / "missing_root_name"

    @property
    def missing_root_description(self) -> Path:
        return self.base_path / "missing_root_description"

    @property
    def missing_root_license(self) -> Path:
        return self.base_path / "missing_root_license"

    @property
    def missing_root_license_name(self) -> Path:
        return self.base_path / "missing_root_license_name"

    @property
    def missing_root_license_description(self) -> Path:
        return self.base_path / "missing_root_license_description"

    @property
    def valid_referenced_generic_data_entities(self) -> Path:
        return self.base_path / "valid_referenced_generic_data_entities"


class InvalidFileDescriptorEntity:

    base_path = INVALID_CRATES_DATA_PATH / "1_file_descriptor_metadata"

    @property
    def missing_entity(self) -> Path:
        return self.base_path / "missing_entity"

    @property
    def invalid_entity_type(self) -> Path:
        return self.base_path / "invalid_entity_type"

    @property
    def missing_entity_about(self) -> Path:
        return self.base_path / "missing_entity_about"

    @property
    def invalid_entity_about(self) -> Path:
        return self.base_path / "invalid_entity_about"

    @property
    def invalid_entity_about_type(self) -> Path:
        return self.base_path / "invalid_entity_about_type"

    @property
    def missing_conforms_to(self) -> Path:
        return self.base_path / "missing_conforms_to"

    @property
    def invalid_conforms_to(self) -> Path:
        return self.base_path / "invalid_conforms_to"


class InvalidDataEntity:

    base_path = INVALID_CRATES_DATA_PATH / "4_data_entity_metadata"

    @property
    def missing_hasPart_data_entity_reference(self) -> Path:
        return self.base_path / "invalid_missing_hasPart_reference"

    @property
    def direct_hasPart_data_entity_reference(self) -> Path:
        return self.base_path / "valid_direct_hasPart_reference"

    @property
    def indirect_hasPart_data_entity_reference(self) -> Path:
        return self.base_path / "valid_indirect_hasPart_reference"

    @property
    def directory_data_entity_wo_trailing_slash(self) -> Path:
        return self.base_path / "directory_data_entity_wo_trailing_slash"

    @property
    def missing_data_entity_encoding_format(self) -> Path:
        return self.base_path / "missing_encoding_format"

    @property
    def invalid_data_entity_encoding_format_pronom(self) -> Path:
        return self.base_path / "invalid_encoding_format_pronom"

    @property
    def invalid_encoding_format_ctx_entity_missing_ws_type(self) -> Path:
        return self.base_path / "invalid_encoding_format_ctx_entity_missing_ws_type"

    @property
    def invalid_encoding_format_ctx_entity_missing_ws_name(self) -> Path:
        return self.base_path / "invalid_encoding_format_ctx_entity_missing_ws_name"

    @property
    def valid_encoding_format_ctx_entity(self) -> Path:
        return self.base_path / "valid_encoding_format_ctx_entity"

    @property
    def valid_encoding_format_pronom(self) -> Path:
        return self.base_path / "valid_encoding_format_pronom"


class InvalidMainWorkflow:

    base_path = INVALID_CRATES_DATA_PATH / "0_main_workflow"

    @property
    def main_workflow_bad_type(self) -> Path:
        return self.base_path / "main_workflow_bad_type"

    @property
    def main_workflow_no_lang(self) -> Path:
        return self.base_path / "main_workflow_no_lang"

    @property
    def main_workflow_no_image(self) -> Path:
        return self.base_path / "main_workflow_no_image"

    @property
    def main_workflow_no_cwl_desc(self) -> Path:
        return self.base_path / "main_workflow_no_cwl_desc"

    @property
    def main_workflow_cwl_desc_bad_type(self) -> Path:
        return self.base_path / "main_workflow_cwl_desc_bad_type"

    @property
    def main_workflow_cwl_desc_no_lang(self) -> Path:
        return self.base_path / "main_workflow_cwl_desc_no_lang"

    @property
    def main_workflow_no_files(self) -> Path:
        return self.base_path / "no_files"

    @property
    def main_workflow_bad_conformsto(self) -> Path:
        return self.base_path / "main_workflow_bad_conformsto"


class WROCInvalidConformsTo:

    base_path = INVALID_CRATES_DATA_PATH / "2_wroc_descriptor"

    @property
    def wroc_descriptor_bad_conforms_to(self) -> Path:
        return self.base_path / "wroc_descriptor_bad_conforms_to"


class WROCInvalidReadme:

    base_path = INVALID_CRATES_DATA_PATH / "1_wroc_crate/"

    @property
    def wroc_readme_not_about_crate(self) -> Path:
        return self.base_path / "readme_not_about_crate"

    @property
    def wroc_readme_wrong_encoding_format(self) -> Path:
        return self.base_path / "readme_wrong_encoding_format"


class WROCNoLicense:

    base_path = INVALID_CRATES_DATA_PATH / "1_wroc_crate/"

    @property
    def wroc_no_license(self) -> Path:
        return self.base_path / "no_license"


class WROCMainEntity:

    base_path = INVALID_CRATES_DATA_PATH / "1_wroc_crate/"

    @property
    def wroc_no_mainentity(self) -> Path:
        return self.base_path / "no_mainentity"


class InvalidProcRC:

    base_path = INVALID_CRATES_DATA_PATH / "3_process_run_crate/"

    @property
    def conformsto_bad_type(self) -> Path:
        return self.base_path / "conformsto_bad_type"

    @property
    def conformsto_bad_profile(self) -> Path:
        return self.base_path / "conformsto_bad_profile"

    @property
    def application_no_name(self) -> Path:
        return self.base_path / "application_no_name"

    @property
    def application_no_url(self) -> Path:
        return self.base_path / "application_no_url"

    @property
    def application_no_version(self) -> Path:
        return self.base_path / "application_no_version"

    @property
    def softwaresourcecode_no_version(self) -> Path:
        return self.base_path / "softwaresourcecode_no_version"

    @property
    def application_id_no_absoluteuri(self) -> Path:
        return self.base_path / "application_id_no_absoluteuri"

    @property
    def application_version_softwareVersion(self) -> Path:
        return self.base_path / "application_version_softwareVersion"

    @property
    def action_no_instrument(self) -> Path:
        return self.base_path / "action_no_instrument"

    @property
    def action_instrument_bad_type(self) -> Path:
        return self.base_path / "action_instrument_bad_type"

    @property
    def action_not_mentioned(self) -> Path:
        return self.base_path / "action_not_mentioned"

    @property
    def action_no_name(self) -> Path:
        return self.base_path / "action_no_name"

    @property
    def action_no_description(self) -> Path:
        return self.base_path / "action_no_description"

    @property
    def action_no_endtime(self) -> Path:
        return self.base_path / "action_no_endtime"

    @property
    def action_bad_endtime(self) -> Path:
        return self.base_path / "action_bad_endtime"

    @property
    def action_no_agent(self) -> Path:
        return self.base_path / "action_no_agent"

    @property
    def action_bad_agent(self) -> Path:
        return self.base_path / "action_bad_agent"

    @property
    def action_no_result(self) -> Path:
        return self.base_path / "action_no_result"

    @property
    def action_no_starttime(self) -> Path:
        return self.base_path / "action_no_starttime"

    @property
    def action_bad_starttime(self) -> Path:
        return self.base_path / "action_bad_starttime"

    @property
    def action_error_not_failed_status(self) -> Path:
        return self.base_path / "action_error_not_failed_status"

    @property
    def action_error_no_status(self) -> Path:
        return self.base_path / "action_error_no_status"

    @property
    def action_no_object(self) -> Path:
        return self.base_path / "action_no_object"

    @property
    def action_no_actionstatus(self) -> Path:
        return self.base_path / "action_no_actionstatus"

    @property
    def action_bad_actionstatus(self) -> Path:
        return self.base_path / "action_bad_actionstatus"

    @property
    def action_no_error(self) -> Path:
        return self.base_path / "action_no_error"

    @property
    def action_obj_res_bad_type(self) -> Path:
        return self.base_path / "action_obj_res_bad_type"

    @property
    def collection_not_mentioned(self) -> Path:
        return self.base_path / "collection_not_mentioned"

    @property
    def collection_no_haspart(self) -> Path:
        return self.base_path / "collection_no_haspart"

    @property
    def collection_no_mainentity(self) -> Path:
        return self.base_path / "collection_no_mainentity"

    @property
    def action_no_environment(self) -> Path:
        return self.base_path / "action_no_environment"

    @property
    def action_bad_environment(self) -> Path:
        return self.base_path / "action_bad_environment"

    @property
    def action_no_containerimage(self) -> Path:
        return self.base_path / "action_no_containerimage"

    @property
    def action_bad_containerimage_url(self) -> Path:
        return self.base_path / "action_bad_containerimage_url"

    @property
    def action_bad_containerimage_type(self) -> Path:
        return self.base_path / "action_bad_containerimage_type"

    @property
    def containerimage_no_additionaltype(self) -> Path:
        return self.base_path / "containerimage_no_additionaltype"

    @property
    def containerimage_bad_additionaltype(self) -> Path:
        return self.base_path / "containerimage_bad_additionaltype"

    @property
    def containerimage_no_registry(self) -> Path:
        return self.base_path / "containerimage_no_registry"

    @property
    def containerimage_no_name(self) -> Path:
        return self.base_path / "containerimage_no_name"

    @property
    def containerimage_no_tag(self) -> Path:
        return self.base_path / "containerimage_no_tag"

    @property
    def containerimage_no_sha256(self) -> Path:
        return self.base_path / "containerimage_no_sha256"

    @property
    def softwareapplication_no_softwarerequirements(self) -> Path:
        return self.base_path / "softwareapplication_no_softwarerequirements"

    @property
    def softwareapplication_bad_softwarerequirements(self) -> Path:
        return self.base_path / "softwareapplication_bad_softwarerequirements"


class InvalidWTROC:

    base_path = INVALID_CRATES_DATA_PATH / "5_workflow_testing_ro_crate/"

    @property
    def testsuite_not_mentioned(self) -> Path:
        return self.base_path / "testsuite_not_mentioned"

    @property
    def testsuite_no_instance_no_def(self) -> Path:
        return self.base_path / "testsuite_no_instance_no_def"

    @property
    def testsuite_no_mainentity(self) -> Path:
        return self.base_path / "testsuite_no_mainentity"

    @property
    def testinstance_no_service(self) -> Path:
        return self.base_path / "testinstance_no_service"

    @property
    def testinstance_no_url(self) -> Path:
        return self.base_path / "testinstance_no_url"

    @property
    def testinstance_no_resource(self) -> Path:
        return self.base_path / "testinstance_no_resource"

    @property
    def testdefinition_bad_type(self) -> Path:
        return self.base_path / "testdefinition_bad_type"

    @property
    def testdefinition_no_engine(self) -> Path:
        return self.base_path / "testdefinition_no_engine"

    @property
    def testdefinition_no_engineversion(self) -> Path:
        return self.base_path / "testdefinition_no_engineversion"

    @property
    def testsuite_bad_instance(self) -> Path:
        return self.base_path / "testsuite_bad_instance"

    @property
    def testsuite_bad_definition(self) -> Path:
        return self.base_path / "testsuite_bad_definition"

    @property
    def testsuite_bad_mainentity(self) -> Path:
        return self.base_path / "testsuite_bad_mainentity"

    @property
    def testinstance_bad_runson(self) -> Path:
        return self.base_path / "testinstance_bad_runson"

    @property
    def testinstance_bad_url(self) -> Path:
        return self.base_path / "testinstance_bad_url"

    @property
    def testinstance_bad_resource(self) -> Path:
        return self.base_path / "testinstance_bad_resource"

    @property
    def testdefinition_bad_conformsto(self) -> Path:
        return self.base_path / "testdefinition_bad_conformsto"

    @property
    def testdefinition_bad_engineversion(self) -> Path:
        return self.base_path / "testdefinition_bad_engineversion"
